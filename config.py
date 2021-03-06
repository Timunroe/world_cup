config = {
    # could reduce db name to just project_name.json
    "project_name": "world_cup",
    "name": "spec",
    "db_name": "world_cup.json",
    "db_fields_dflt": {
        'desc_user': '',
        'draft_user': 0,  # int 0:published, 1-2: draft
        'rank': 0, # int
        'rank_time': 0, # int
        'label_user': '',
        'title_user': '',
        'tags_user': [], # list of strings
    },
    "db_fields": 
    [
        'asset_id',
        'author_api',
        'caption_api',
        'categories_api',
        'label_api',
        'source_api',
        'desc_api',
        'draft_api',
        'link',
        'img_api',
        'img_api_thumb',
        'pubdate_api',
        'region_api',
        'site_api',
        'tags_api',
        'timestamp',
        'title_api'
    ],
    "apis":
        [
            {
                "url": 'http://api.zuza.com/search/article/default?&category=sports&subcategory=soccer&pageIndex=1&location=hamilton&sort=datedesc&pageSize=15&startindex=1&endindex=15',
                "filter": ["searchResultView"]
            },
            {
                "url": 'http://api.zuza.com/search/article/default?&category=sports&pageIndex=1&location=hamilton&sort=datedesc&pageSize=10&startindex=1&endindex=10',
                "filter": ["searchResultView"]
            }
    ],
    "munge": []
}

# BY KEYWORD
# http://api.zuza.com/search/article/default?q=KeywordsAlias:”XXXXX"&pageIndex=1&location=hamilton&sort=datedesc&pageSize=5startindex=1&endindex=5
# BY CATEGORY/SUBCATEGORY
# http://api.zuza.com/search/article/default?&category=XXXX&subcategory=XXXX&pageIndex=1&location=hamilton&sort=datedesc&pageSize=10&startindex=1&endindex=10
# BY AUTHOR: where guid: is author page key.
# http://api.zuza.com/search/article/default?guid=25a2fb14-ae69-41f2-beab-bdda47383f93&pageIndex=1&location=hamilton&sort=datedesc&pageSize=15&startindex=1&endindex=5