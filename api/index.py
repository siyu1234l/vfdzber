from flask import Flask, request

app = Flask(__name__)


@app.route('/search')
def hello_world():  # put application's code here
    from duckduckgo_search import ddg

    keywords = request.args.get('q')
    print(request.args.get('max_results'))
    max_results = int(request.args.get('max_results') or "3")
    results = ddg(keywords, region='wt-wt', max_results=max_results)
    print(results)
    return results


if __name__ == '__main__':
    app.run(host='0.0.0.0')
