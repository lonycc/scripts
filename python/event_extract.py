import re
import pymongo
import urllib.parse
import requests
from bs4 import BeautifulSoup as bs

class MakeDataset:
    def __init__(self, start_url):
        mongo_host = '127.0.0.1' # 你数据库的ip
        mongo_port = 27017 #你数据库端口
        mongo_db = 'news' #数据库名称
        mongo_col = 'news_data' #数据表名称
        client = pymongo.MongoClient(f'mongodb://{mongo_host}:{mongo_port}')
        self.db = client[mongo_db]
        self.col = self.db[mongo_col]
        self.session = requests.Session()
        self.start_url = start_url

    def start_request(self):
        soup = self.get_soup(self.start_url)
        links = soup.findAll('a')
        for link in links:
            self.parse_article(link.get('href'))

    def parse_article(self, link):
        if link is None:
            return
        if re.match(r'http://(.*?)/content_\d+\.htm$', link) is None:
            return
        soup = self.get_soup(link)
        content = soup.find('div', class_='content')
        self.save(link, content.text)


    def get_soup(self, link):
        content = self.session.get(link).content
        content = str(content, 'utf-8')
        return bs(content, 'html.parser')

    def save(self, url, content):
        data = {'url':url, 'content':content}
        self.col.insert(data)

'''中文复句整理及模板'''
class EventsExtraction:
    def __init__(self):
        self.but_wds = self.pattern_but()
        self.seq_wds = self.pattern_seq()
        self.condition_wds = self.pattern_condition()
        self.more_wds = self.pattern_more()

        self.but_patterns = self.create_pattern(self.but_wds)
        self.seq_patterns = self.create_pattern(self.seq_wds)
        self.condition_patterns = self.create_pattern(self.condition_wds)
        self.more_patterns = self.create_pattern(self.more_wds)
    
    '''转折事件'''
    def pattern_but(self):
        return [
            [['与其'], ['不如'],'but'],
            [['虽然','尽管','虽'],['但也','但还','但却','但'],'but'],
            [['虽然','尽管','虽'],[ '但','但是也','但是还','但是却',],'but'],
            [['不是'],['而是'],'but'],
            [['即使','就算是'],['也','还'],'but'],
            [['即便'],['也','还'],'but'],
            [['虽然','即使'],['但是','可是','然而','仍然','还是','也', '但'],'but'],
            [['虽然','尽管','固然'],['也','还','却'],'but'],
            [['与其','宁可'],['决不','也不','也要'],'but'],
            [['与其','宁肯'],['决不','也要','也不'],'but'],
            [['与其','宁愿'],['也不','决不','也要'],'but'],
            [['虽然','尽管','固然'],['也','还','却'],'but'],
            [['不管','不论','无论','即使'],['都', '也', '总', '始终', '一直'],'but'],
            [['虽'],['可是','倒','但','可','却','还是','但是'],'but'],
            [['虽然','纵然','即使'],['倒','还是','但是','但','可是','可','却'],'but'],
            [['虽说'],['还是','但','但是','可是','可','却'],'but'],
            [['无论'],['都','也','还','仍然','总','始终','一直'],'but'],
            [['与其'],['宁可','不如','宁肯','宁愿'],'but']
        ]
    
    '''顺承事件'''
    def pattern_seq(self):
        return [
            [['又', '再', '才', '并'], ['进而'], 'sequence'],
            [['首先', '第一'], ['其次', '然后'], 'sequence'],
            [['首先', '先是'], ['再', '又', '还', '才'], 'sequence'],
            [['一方面'], ['另一方面', '又', '也', '还'], 'sequence']
        ]

    '''并列事件'''
    def pattern_more(self):
        return [
            [['不但', '不仅'], ['并且'], 'more'],
            [['不单'], ['而且', '并且', '也', '还'], 'more'],
            [['不但'], ['而且', '并且', '也', '还'], 'more'],
            [['不管'], ['都', '也', '总', '始终', '一直'], 'more'],
            [['不光'], ['而且', '并且', '也', '还'], 'more'],
            [['虽然', '尽管'], ['不过'], 'more'],
            [['不仅'], ['还', '而且', '并且', '也'], 'more'],
            [['不论'], ['还是', '也', '总', '都', '始终', '一直'], 'more'],
            [['不只'], ['而且', '也', '并且', '还'], 'more'],
            [['不但', '不仅', '不光', '不只'], ['而且'], 'more'],
            [['尚且', '都', '也', '又', '更'], ['还', '又'], 'more'],
            [['既然', '既',], ['就', '便', '那', '那么', '也', '还'], 'more'],
            [['无论', '不管', '不论', '或'], ['或'], 'choice'],
            [['或是'], ['或是'], 'choice'],
            [['或者', '无论', '不管', '不论'], ['或者'], 'choice'],
            [['不是'], ['也'], 'choice'],
            [['要么', '或者'], ['要么', '或者'], 'choice']
        ]

    '''条件事件'''
    def pattern_condition(self):
        return [
            [['除非'], ['否则', '才', '不然', '要不'], 'condition'],
            [['除非'], ['否则的话'], 'condition'],
            [['还是', '无论', '不管'], ['还是', '都', '总'], 'condition'],
            [['既然'], ['又', '且', '也', '亦'], 'condition'],
            [['假如'], ['那么', '就', '也', '还'], 'condition'],
            [['假若', '如果'], ['那么', '就', '那', '则', '便'], 'condition'],
            [['假使', '如果'], ['那么', '就', '那', '则', '便'], 'condition'],
            [['尽管', '如果'], ['那么', '就', '那', '则', '便'], 'condition'],
            [['即使', '就是'], ['也', '还是'], 'condition'],
            [['如果', '既然'], ['那么'], 'condition'],
            [['如', '假设'], ['则', '那么', '就', '那'], 'condition'],
            [['如果', '假设'], ['那么', '则', '就', '那'], 'condition'],
            [['万一'], ['那么', '就'], 'condition'],
            [['要是', '如果'], ['就', '那'], 'condition'],
            [['要是', '如果', '假如'], ['那么', '就', '那', '的话'], 'condition'],
            [['一旦'], ['就'], 'condition'],
            [['既然', '假如', '既', '如果'], ['则','就'], 'condition'],
            [['只要'], ['就', '便', '都', '总'], 'condition'],
            [['只有'], ['才', '还'], 'condition']
        ]

    '''编译模式'''
    def create_pattern(self, wds):
        patterns = []
        for wd in wds:
            pre = wd[0]
            pos = wd[1]
            pattern = re.compile(r'({0})(.*)({1})([^？?！!。；;：:\n\r,，]*)'.format('|'.join(pre), '|'.join(pos)))
            patterns.append(pattern)
        return patterns

    '''文章分句处理, 切分长句，冒号，分号，感叹号等做维护标识'''
    def split_sents(self, content):
        return [sentence.replace('　','') for sentence in re.split(r'[？?！!。；;：:\n\r]', content) if sentence]

    '''模式匹配'''
    def pattern_match(self, patterns, sent):
        datas = {}
        max = 0
        for p in patterns:
            ress = p.findall(sent)
            if ress:
                for res in ress:
                    data = {'pre_wd': res[0], 'pre_part': res[1], 'post_wd': res[2], 'post_part ': res[3]}
                    len_res = len(res[0] + res[2])
                    if len_res > max:
                        datas = data
                        max = len_res
        return datas
    
    '''基于模式，抽取出相应的四元组'''
    def extract_tuples(self, sent):
        but_tuples = self.pattern_match(self.but_patterns, sent)
        condition_tuples = self.pattern_match(self.condition_patterns, sent)
        seq_tuples = self.pattern_match(self.seq_patterns, sent)
        more_tuples = self.pattern_match(self.more_patterns, sent)
        return but_tuples, condition_tuples, seq_tuples, more_tuples

    '''处理主函数'''
    def extract_main(self, content):
        sents = self.split_sents(content)
        datas = []
        for sent in sents:
            data = {}
            data['sent'] = sent
            but_tuples, condition_tuples, seq_tuples, more_tuples = self.extract_tuples(sent)
            if but_tuples:
                data['type'] = 'but'
                data['tuples'] = but_tuples
            if condition_tuples:
                data['type'] = 'condition'
                data['tuples'] = condition_tuples
            if seq_tuples:
                data['type'] = 'seq'
                data['tuples'] = seq_tuples
            if more_tuples:
                data['type'] = 'more'
                data['tuples'] = more_tuples
            if 'type' in data:
                datas.append(data)
        return datas

'''基于给定语料与模板的事件抽取，假定你选择的是Mongodb数据库'''
class TextMining:
    def __init__(self):
        mongo_host = '127.0.0.1' # 你数据库的ip
        mongo_port = 27017 #你数据库端口
        mongo_db = 'news' #数据库名称
        mongo_col = 'news_data' #数据表名称
        #username = urllib.parse.quote_plus("root")#用户名
        #password = urllib.parse.quote_plus("12345678") #密码
        #client = pymongo.MongoClient('mongodb://{}:{}@{}:{}'.format(username, password, mongo_host, mongo_port))
        client = pymongo.MongoClient(f'mongodb://{mongo_host}:{mongo_port}')
        self.db = client[mongo_db]
        self.col = self.db[mongo_col]
        self.extractor = EventsExtraction()

    '''批量跑数据库中的数据，并插入相应数据库当中'''
    def process_mongonews(self):
        count = 0
        for item in self.col.find():
            content = item['content']
            url = item['url']
            count += 1 
            try:
                datas = self.extractor.extract_main(content)
                if datas:
                    data = {}
                    data['url'] = url
                    data['data'] = datas
                    self.db['event_extract'].insert(data)
            except Exception as e:
                print(e)
            if count % 10000 == 0:
                print(count)

if __name__ == '__main__':
    #dataset = MakeDataset('http://www.sabc.com')
    #dataset.start_request()
    handler = TextMining()
    handler.process_mongonews()
