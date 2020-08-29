[![Travis (.org)](https://img.shields.io/travis/avdata99/ckanext-datasetpreview?style=for-the-badge)](https://travis-ci.org/github/avdata99/ckanext-datasetpreview)
[![GitHub All Releases](https://img.shields.io/github/downloads/avdata99/ckanext-datasetpreview/total?style=for-the-badge)](https://github.com/avdata99/ckanext-datasetpreview/releases)
[![GitHub Issues](https://img.shields.io/github/issues/avdata99/ckanext-datasetpreview?style=for-the-badge)](https://github.com/avdata99/ckanext-datasetpreview/issues)
[![GitHub PR](https://img.shields.io/github/issues-pr/avdata99/ckanext-datasetpreview?style=for-the-badge)](https://github.com/avdata99/ckanext-datasetpreview/pulls)
[![Licence](https://img.shields.io/github/license/avdata99/ckanext-datasetpreview?style=for-the-badge)](https://github.com/avdata99/ckanext-datasetpreview/blob/master/LICENSE)
[![Pypi py version](https://img.shields.io/pypi/pyversions/ckanext-datasetpreview?style=for-the-badge)](https://pypi.org/project/ckanext-datasetpreview/)
[![Last Commit](https://img.shields.io/github/last-commit/avdata99/ckanext-datasetpreview?style=for-the-badge)](https://github.com/avdata99/ckanext-datasetpreview/commits/master)

# CKAN dataset preview

Still in a develpment status

Adds automatically charts for all datasets in the dataset list.
Uses `messytables` to discover field types.

## How to set up?

```json
extras["dataset_preview"] = {
    "fields": ["Field1", "Field2"],
    "chart_type": "Bar", // Allows 'Pie', 'Bar', 'Column'
    "url": "Use only if you want specific CSV, if not it takes the first CSV resource",
    "height": 450,  // pixels
}
```
If you don't setup each dataset it will show the first CSV resource in the dataset (using the first two columns)


![dataset-list](ckanext/datasetpreview/captures/dataset-list.png)
