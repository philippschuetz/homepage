# homepage
## The build script
### Placeholders
Placeholders are replaced when building the project. There are different types of placeholders:
The content placeholder is used in `base.html` to define the position of the inserted page content.
Template placeholders are used to insert content from html files (components) in the templates directory.
The name of the template placeholder can be derived from the name of the template file.
E.g. if the component file is called `foo.html` the placeholder is `<!--components-foo-->`.