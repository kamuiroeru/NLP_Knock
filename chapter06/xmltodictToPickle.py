import xmltodict, pickle

inputxml = 'nlp.txt.xml'

pickle.dump(xmltodict.parse(open('nlp.txt.xml').read()),
            open('xml.pickle', 'wb'))
