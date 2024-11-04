import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    self_viewed_authors = views[views['author_id'] == views['viewer_id']]['author_id'].unique()
    result = pd.DataFrame({'id': sorted(self_viewed_authors)})

    return result
