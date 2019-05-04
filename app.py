import connexion
from connexion.resolver import RestyResolver
from services.provider import ItemsProvider
from flask_injector import FlaskInjector
from injector import Binder

def configure(binder: Binder) -> Binder:
    binder.bind(
        ElasticSearchIndex,
        ElasticSearchIndex(
            ElasticSearchFactory(
                os.environ['ELASTICSEARCH_HOST'],
                os.environ['ELASTICSEARCH_PORT'],
            ),
            'rooms',
            'room',
            room_mapping
        )
    )

    return binder

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('indexer.yaml', resolver=RestyResolver('api'))
    #FlaskInjector(app=app.app, modules=[configure])
    app.run(port=8080)
