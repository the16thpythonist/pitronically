### 0.1.0.0 - initial version - 16.05.2019

- The most important models are implemented. This includes the main "Entry" and the 
inheriting "Project" Model. The Project model is used to represent a blog post showcasing 
a project.
    - The project model even supports a WYSIWYG Editor on the admin backend and a file 
    browser for user friendly post creation
- The Detail view for a single Project model object works. It displays the main thumbnail 
The title and subtitle, the author and the date of publishing, the content and the tags.
- A first version of the list view for the project type works. All the most recent projects 
are represented in a list, showing the author, date, preview thumbnail, title and subtitle 
for each post.
- The main HTML and CSS template for the site
- Using the NavbarMixin and SidebarMixin. Every view has a reusable access to displaying 
common elements.
