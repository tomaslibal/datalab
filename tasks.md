# Priorities

- [ ] [lab] add "new dataset" page
- [ ] [lab/api] change path datapoints/as_csv to /api/datapoints/download/wswtm_format
- [ ] [lab] add url handler for label/:id for editing an existing label
- [ ] [lab] enable the checkboxes in datapoint detail view to add/remove the datapoint from a dataset
- [ ] [lab] display succinctly the datasets to which a datapoint belongs in datapoints.html page 

# Backlog:

- [ ] [lab] add "speed labeller" page
- [ ] [lab] file import reads the dataset checkboxes values
- [ ] [lab/api] download all datapoints from all datasets
- [ ] [lab/api] download datapoints that are not in any dataset
- [ ] [lab/api] add path label/:id/datapoints for displaying a list of datapoints using the given label
- [ ] [lab] enable the "see all" button on the homepage
- [ ] [lab] add a parent attribute to Label
- [ ] [lab] each datapoint has separate labels for each dataset it is in
- [ ] [lab/api] label can be labelled as "wrong" or "typical" (as a sort of voting)
- [ ] [lab] add n-gram entity
- [ ] [lab] add text entity (or just use 1-gram instead?)
- [ ] [lab] add a confirmation popup for the delete actions
- [ ] [lab] add similar datapoints abstraction to Entity - so that any Entity type can have the concept of "similar" (e.g. Lehvenstein for text based Entities)
- [ ] [lab] add similar images (based on Mean Value Hashing algorithm)
- [ ] [lab] add a proper implementation of the Mean Value Hashing algorithm
- [ ] [lab] add gzipping for data downloads
- [ ] [lab] add a config for a proxy server for deploying datalab to production environments

# Done:

- [x] ~~add UserDefinedEntities model (user cannot use the predefined entities out of the box but must define their own entities)~~
- [x] ~~update datapoint from datapoint detail (POST handler)~~
- [x] ~~add search/ path which takes a search query and returns results~~
- [x] ~~add pagination to labels/~~
- [x] ~~add path label/:id/delete for deleting a label~~
- [x] ~~add pagination to datapoints/~~
- [x] ~~add karma config~~
- [x] ~~write 1st jasmine test~~
- [x] ~~add a ImageEntityProcessor class~~
- [x] ~~add Dataset model~~
- [x] ~~add many-to-many relation from Datapoint to Dataset (i.e. each datapoint can belong to many datasets)~~
- [x] ~~add entity~~
- [x] ~~add dataset checkbox to the import page~~

# Discarded:

~~[] add an abstract class Entity~~
