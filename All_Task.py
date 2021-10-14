#https://www.merakilearn.org/course/76/exercise/1930
def scrape_top_list():
    import json
    import requests
    from bs4 import BeautifulSoup
    url = BeautifulSoup(requests.get("https://www.imdb.com/india/top-rated-indian-movies/").content,"html.parser").find('tbody', class_="lister-list")
    title = url.find_all('td',class_='titleColumn')
    rating = url.find_all('td',class_='ratingColumn imdbRating')
    k = [i.strong.text for i in rating]
    movies = []
    ind = 1
    for i in title:
        b = {}
        b["Name"] = i.a.text
        b["year"] = i.span.text.replace('(',"").replace(")","")
        b["postion"] = ind
        b["Rating"] = k[ind-1]
        b["url"] = "https://www.imdb.com" + i.a["href"]
        ind += 1
        movies.append(b)
    vk = open("v.json","w")
    json.dump(movies,vk,indent=4)
    return movies


def scrape_movie_details(movie_url):
    import json
    try:
        f = open(movie_url[-10:-1],'r').read()
        return json.loads(f)  
    except:
        import requests
        from bs4 import BeautifulSoup
        v = {}
        url = BeautifulSoup(requests.get(movie_url).content,"html.parser")
        u = url.find_all('li',class_='ipc-metadata-list__item')
        name = url.find('h1').text
        v['Name'] = name
        director = url.find('ul', class_='ipc-metadata-list ipc-metadata-list--dividers-all StyledComponents__CastMetaDataList-y9ygcu-10 cbPPkN ipc-metadata-list--base')
        die = director.find_all('li', class_='ipc-metadata-list__item')
        vvvv = url.find('div',class_="styles__MetaDataContainer-sc-12uhu9s-0 cgqHBf")
        lils = []
        for i in die:
            if i.span != None and i.a != None:
                if i.span.text == 'Director':
                    k = i.find_all('a')
                    for j in k:
                        lils.append(j.text)
                    v[i.span.text] = lils
        details = url.find('ul',class_='ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base')
        coy = details.find_all('li')
        gghgh = details.find('ul',class_="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base")
        lll = []
        if gghgh != None:
            if gghgh.li != None:
                if gghgh.li.a !=None:
                    v['Release_Date'] = gghgh.li.a.text
        for i in coy:
            if i.span != None and i.a != None:
                if i.span.text == 'Country of origin':
                    v['Country'] = i.a.text
                elif i.span.text == "Language":
                    lll.append(i.a.text)
                    v['Language'] = lll
                else:
                    for i in vvvv:
                        lis = []
                        if i.span != None and i.a != None:
                            if i.span.text == 'Language':
                                lis.append(i.a.text)
                                v[i.span.text] = i.a.text
        v["poster_image_url"] = ("https://www.imdb.com" + url.find('a',class_='ipc-lockup-overlay ipc-focusable')['href'])
        v["bio"] = url.find('span',class_='GenresAndPlot__TextContainerBreakpointXS_TO_M-cum89p-0 dcFkRD').text
        runtim = url.find('ul',class_='ipc-inline-list ipc-inline-list--show-dividers TitleBlockMetaData__MetaDataList-sc-12ein40-0 dxizHm baseAlt').find_all('li')
        kk = []
        for i in runtim:
            kk.append(i.text)
        v["Runtime"] = kk[-1]
        gene = url.find('div', class_='ipc-chip-list GenresAndPlot__GenresChipList-cum89p-4 gtBDBL')
        gene2 = url.find('div', class_='ipc-chip-list GenresAndPlot__OffsetChipList-cum89p-5 dMcpOf')
        if gene != None:
            genre = gene.find_all('a')
            l = []
            for i in genre:
                if i != None:
                    l.append(i.text)
            v['genre'] = l
        else:
            genre = gene2.find_all('a')
            l = []
            for i in genre:
                if i != None:
                    l.append(i.text)
            v['genre'] = l
        topcast = url.find('div',class_="ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--wraps-at-above-l title-cast__grid").find_all('div',class_="StyledComponents__CastItemWrapper-y9ygcu-7 hTEaNu")
        topcastlis = []
        for i in topcast:
            k = i.find('div',class_='StyledComponents__CastItemSummary-y9ygcu-9 fBAofn')
            if k.a != None:
                topcastlis.append(k.a.text)
        v['TopCast'] = topcastlis
        vvvvv = url.find('li',class_='ipc-metadata-list__item ipc-metadata-list-item--link')
        f = open(movie_url[-10:-1],'w')
        json.dump(v,f,indent=4)
        return v

  def get_movie_list_details(movies_lis):
    import json
    k = {}
    b = []
    a = 1
    jk = open("sale.json","w")
    for i in movies_lis:
        c = scrape_movie_details(i['url'])
        b.append(c)
        k[a] = c
        a+=1
        if a % 10 == 0:
            time.sleep(2)
    json.dump(k,jk,indent=4)
    return b
jj = json.loads(open("vk.json","r").read())
get_movie_list_details(jj)


# w = open("Data.json","r").read()
# baa = json.loads((w))
# ba = list(baa.keys())
# b = []
# for i in ba:
#     b.append(baa[i])
# movies_list = b
# def analyse_movies_language(movies_list):
#     k = {}
#     b = []
#     for i in movies_list:
#         b.extend(i['Language'])
#     c = list(set(b))
#     for i in c:
#         k[i] = b.count(i)
#     print(k)

# # analyse_movies_language(b)

# def director_analysis(movies_list):
#     k = {}
#     b = []
#     for i in movies_list:
#         b.append(i['Director'])
#     c = list(set(b))
#     for i in c:
#         k[i] = b.count(i)
#     print(k)

# director_analysis(b)



