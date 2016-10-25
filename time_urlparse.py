import timeit


result = timeit.timeit(
    'urlparse.clear_cache(); urlparse.urlparse(url)',
    setup="import urlparse; url = 'https://www.parsely.com:8080/plogger/?rand=1475090003784&idsite=naitreetgrandir.com&url=http%3A%2F%2Fnaitreetgrandir.com%2Fblogue%2F2015%2F10%2F15%2Fdeuil-perinatal-personne-a-l-abri%2F&urlref=http%3A%2F%2Fm.facebook.com%2F&screen=360x640%7C360x640%7C32&data=%7B%22parsely_uuid%22%3A%22b20bc9b9-7078-4df9-bd74-d86375b5f57a%22%2C%22parsely_site_uuid%22%3A%22a7049486-20cb-492a-b49a-fff6a9002d54%22%7D&sid=1&surl=http%3A%2F%2Fnaitreetgrandir.com%2Fblogue%2F2015%2F10%2F15%2Fdeuil-perinatal-personne-a-l-abri%2F&sref=http%3A%2F%2Fm.facebook.com%2F&sts=1475090003770&slts=0&title=Deuil+p%C3%A9rinatal%3A+personne+n%27est+%C3%A0+l%27abri&date=Wed+Sep+28+2016+15%3A13%3A23+GMT-0400+(EDT)&action=pageview&metadata=%7B%22title%22%3A%22Deuil+p%C3%A9rinatal%3A+personne+n%27est+%C3%A0+l%27abri%22%2C%22link%22%3A%22http%3A%2F%2Fnaitreetgrandir.com%2Fblogue%2F2015%2F10%2F15%2Fdeuil-perinatal-personne-a-l-abri%2F%22%2C%22image_url%22%3A%22http%3A%2F%2Fnaitreetgrandir.com%2FDocumentsNG%2FImages%2FImagesPrincipalePetite%2Fdeuil-perinatal-personne-a-l-abri.jpg%22%2C%22section%22%3A%22%2Fblogue%22%2C%22tags%22%3A%5B%22blogue%22%5D%2C%22authors%22%3A%5B%22Jos%C3%A9e+Bournival%22%5D%2C%22page_type%22%3A%22post%22%7D HTTP/1.1 || 200 || 229 || http://naitreetgrandir.com/blogue/2015/10/15/deuil-perinatal-personne-a-l-abri/'",
    number=100000
)

print('Fast: {}'.format(result))

result = timeit.timeit(
    'urlparse.clear_cache(); urlparse.urlparse(url)',
    setup="import urllib.parse as urlparse; url = 'https://www.parsely.com:8080/plogger/?rand=1475090003784&idsite=naitreetgrandir.com&url=http%3A%2F%2Fnaitreetgrandir.com%2Fblogue%2F2015%2F10%2F15%2Fdeuil-perinatal-personne-a-l-abri%2F&urlref=http%3A%2F%2Fm.facebook.com%2F&screen=360x640%7C360x640%7C32&data=%7B%22parsely_uuid%22%3A%22b20bc9b9-7078-4df9-bd74-d86375b5f57a%22%2C%22parsely_site_uuid%22%3A%22a7049486-20cb-492a-b49a-fff6a9002d54%22%7D&sid=1&surl=http%3A%2F%2Fnaitreetgrandir.com%2Fblogue%2F2015%2F10%2F15%2Fdeuil-perinatal-personne-a-l-abri%2F&sref=http%3A%2F%2Fm.facebook.com%2F&sts=1475090003770&slts=0&title=Deuil+p%C3%A9rinatal%3A+personne+n%27est+%C3%A0+l%27abri&date=Wed+Sep+28+2016+15%3A13%3A23+GMT-0400+(EDT)&action=pageview&metadata=%7B%22title%22%3A%22Deuil+p%C3%A9rinatal%3A+personne+n%27est+%C3%A0+l%27abri%22%2C%22link%22%3A%22http%3A%2F%2Fnaitreetgrandir.com%2Fblogue%2F2015%2F10%2F15%2Fdeuil-perinatal-personne-a-l-abri%2F%22%2C%22image_url%22%3A%22http%3A%2F%2Fnaitreetgrandir.com%2FDocumentsNG%2FImages%2FImagesPrincipalePetite%2Fdeuil-perinatal-personne-a-l-abri.jpg%22%2C%22section%22%3A%22%2Fblogue%22%2C%22tags%22%3A%5B%22blogue%22%5D%2C%22authors%22%3A%5B%22Jos%C3%A9e+Bournival%22%5D%2C%22page_type%22%3A%22post%22%7D HTTP/1.1 || 200 || 229 || http://naitreetgrandir.com/blogue/2015/10/15/deuil-perinatal-personne-a-l-abri/'",
    number=100000
)

print('Slow: {}'.format(result))
