from pathlib import Path

import kedro
from kedro.framework.context import KedroContext

from src.catalogs.catalog import catalog_dict
from src.pipelines.pipeline import pipelines_dict
from src.hooks.add_catalog_dict import AddCatalogDictHook
from src.hooks.register_pipelines import RegisterPipelinesHook


class ProjectContext(KedroContext):

    project_name = "KedroProject"
    project_version = kedro.__version__
    package_name = "nodes"
    hooks = (
        AddCatalogDictHook(catalog_dict),
        RegisterPipelinesHook(pipelines_dict),
    )


if __name__ == "__main__":
    project_context = ProjectContext(Path.cwd())
    project_context.run()
