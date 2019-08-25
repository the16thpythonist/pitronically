### 0.1.0 - initial version - 16.05.2019

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

### 0.1.1 - 18.07.2019

- Replaced the WYSIWYG Editor package with a new one called "ckeditor", because of its possiblity 
to define custom storages for image files used within the editor. This feature will be needed to make 
the editor work in production, when the media files are saved in AMAZON AWS buckets
- Replaced the previous file management package with django-filer, also due to its compatibility 
with AWS buckets.
- Fixed the bug with no image being able to be uploaded to any user model
- Reworked the image handling for user models: A full size profile picture can now be uploaded and the 
50x50px profile icon is being computed during the model save process.

### 0.1.2 - 21.07.2019

- Added new fields to the user model, which are shown in the "Profile" section of the admin field
 - introduction: Short text about yourself
 - age
 - country
 - profession
- Added an Impressum static page 
- User profiles can now be viewed.
 - My own user profile now also acts as an about me page
- Header site logo is now a link

### 0.1.3 - 24.07.2019

- Minor style tweaks on the project post titles and the list view template
- Bug fix: Tags are now being displayed for each post, although they do not link to anything yet
- Added a new special styling div class "summary", which can be added to the beginning of a post
to write a short summary of whats to come
- Style tweaked the ratio between the main content and the sidebar widget
- Turned off debug mode in production settings

### 0.1.4 - 28.07.2019

- Style tweaks:
 - Added an indicator to the thumbnail of the project list view which says "Project". This is not 
 so relevant now, as there is nothing else but projects but it will come in handy later on, when 
 there are more post types but one
 - Reduced size of some fonts
- Added a Javascript package "prism", which now allows to display syntax highlighted code 
snippets in posts
 - had to remove the code snippet editor from CKEditor for that
- The list display of projects in the django admin panel now actually shows the names of the posts, 
the author and the creation date, instead of just "Project(<index>) object"

### 0.1.5 - 25.08.2019 

- Added the "Tutorial" post type to the website
 - These kind of posts are supposed to be more educational and explanatory of a certain topic instead 
 of merely being a showcase like "Project" 
 - As of for now, it uses the same styling and logic as the Project post type.
