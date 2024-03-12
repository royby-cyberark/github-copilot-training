from pydantic import BaseModel

# This is a response from github's graphql API for a commit search query

d = {
    'search': {
        'nodes': [
            {
                'defaultBranchRef': {
                    'target': {
                        'history': {
                            'nodes': [
                                {
                                    "committedDate": "2023-12-05T11:37:10Z",
                                    "message": "some comment message",
                                    "additions": 160,
                                    "deletions": 1,
                                    "author": {
                                        "name": "John Doe",
                                        "email": "john.doe@acme.com"
                                    }
                                },
                            ],
                            'pageInfo': {
                                'endCursor': None,
                                'hasNextPage': False
                            },
                            'totalCount': 0
                        }
                    }
                },
                'name': 'PreRecieveHooks'
            }
        ],
        'pageInfo': {
            'endCursor': 'A1Bcd23eFgH=', 
            'hasNextPage': False
        }
    }
}
