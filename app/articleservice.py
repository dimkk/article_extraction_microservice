from datetime import date, datetime
from flask import Flask
from flask_restful import Resource, Api, reqparse
from newspaper import Article


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('url', required=True, location='args')

class ArticleService(Resource):
    def get(self):
        args = parser.parse_args()
        url = args['url']
        article = Article(url)
        article.download()
        article.parse()
        result = {}
        result['authors'] = article.authors
        result['publish_date'] = article.publish_date.isoformat()
        result['top_image'] = article.top_image
        result['text'] = article.text

        return {'hello': result}

api.add_resource(ArticleService, '/','/article')

if __name__ == '__main__':
    app.run(debug=True)
