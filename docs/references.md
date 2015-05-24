# Reference manager

**Labii reference manager - IMDb for research papers.**

![labii-reference-manager-home](https://labiiblog.files.wordpress.com/2015/05/labii-reference-manager-home.png)

Labii reference manager is a online platform for commenting, rating and managing research papers. There are > 3000 papers released every day from Pubmed, it is very difficult to find the good relevant papers to read. To select a good paper is somehow similar in the way to choose a good movie. It does not necessary a famous director or producer will always release good movies. IMDb is a good platform for people to rate the movies after they watched them. And the IMDb score, in turn, benefits those who have not watched the movie in choosing good movies.

IMDb utilize everyone's knowledge in judging movies. The same system can be applies to research papers. A such system can benefit the readers in choosing right papers to read and understanding the paers by reading others' comments. More importantly, it connects the authors and readers, and a reader with other readers.

To access the reference manager in [labii.com](http://www.labii.com), click the bar icon on the top left and select the **Reference manager** from the dropdown menu.

To use the refernce manager, click **My libraries** from navigation bar. Most of functions only available after login.

---

### Table of content

1. [Interface](#interface)
	* [Sidebar](#interface-sidebar)
	* [Paper list](#interface-paper-list)
	* [Details](#interface-details)
2. [Search papers](#search-papers)
	* [Search history](#search-papers-history)
3. [Paper details](#paper-details)
	* [Title](#paper-details-title)
	* [Metrics](#paper-details-metrics)
	* [Authors](#paper-details-authors)
	* [Abstract](#paper-details-abstract)
	* [Paper links](#paper-details-paper-links)
	* [Comments](#paper-details-comments)
	* [Discussion](#paper-details-discussion)
4. [Libraries](#libraries)
	* [Add a folder]()
	* [Edit a folder]()
	* [Delete a folder]()
	* [Folder details]()
	* [Add papers to a folder]()
	* [View papers from a folder]()
	* [Delete papers from a folder]()
	* [Import papers from BibTex file]()
	* [Import papers from Mendeley]()
	* [Export papers to BibTex file]()
	* [View shared folders]()
5. [Topics]()
	* [Create a topic]()
	* [View papers from a topic]()
	* [Topic details]()
	* [View shared topics]()
6. [Journals]()
	* [Browse all journals]()
	* [View papers from a journal]()
	
---

### Interface

The labii reference manager interface can be separated into 3 columns. **Sidebar** (left), **Paper list** (middle), and **Details** (right).

![labii-references-manager](https://labiiblog.files.wordpress.com/2015/05/labii-references-manager.png)

#### Sidebar<a name="interface-sidebar"></a>

The sidebar in left side was designed for easy data access. It includes:

* `Search bar` - search papers from pubmed
* `Libraries` - personal paper collections
* `Topics` - track the most recent papers of interest
* `Journals` - follow papers by journals
* `Search Histroy` - your search history

> Note: each panel can be **Expand** or **Collapse** by clicking the panel name. Details can be found bellow.

#### Paper list<a name="interface-paper-list"></a>

![labii-reference-manager-paper-list](https://labiiblog.files.wordpress.com/2015/05/labii-reference-manager-paper-list.png)

A list of papers will be displayed in the middle column.

There is one paper per row, on each row:

* A check box to select / unselect the paper
* Paper title
* Paper authors (Only the first two authors and the last author would be displayed)
* Journal info
* Rating score

The selected papers can be copied to one other foler or deleted from the folder. Click the check box on the top to select or unselect all papers in the page.

#### Details<a name="interface-details"></a>

The right column shows the details of the item (folder, topic, journal, search history) that clicked on the left sidebar column. Some action buttons also included.

If a paper is clicked, the right column will show the details of a paper. The details will be discussed bellow.

---

### Search papers

Papers can be search directly from labii reference manager. Simply put the query into search box and our webstie will display the data for you. We are using pubmed searching API. Only the papers from pubmed can be found. We are working on it to include more data.

#### Search history<a name="search-papers-history"></a>

![labii-reference-manager-search-history](https://labiiblog.files.wordpress.com/2015/05/labii-reference-manager-search-history.png)

Your searching queries will be stored in our database and display it back to you for your easy access. If you did not login, your IP will be used to link to the queries.

---

### Paper details

When a paper is clicked, the details of the paper will be displayed in the right column. These includes:

####Title<a name="paper-details-title"></a>

The title of the paper

####Metrics<a name="paper-details-metrics"></a>

![labii-reference-manager-paper-details-metrics](https://labiiblog.files.wordpress.com/2015/05/labii-reference-manager-paper-details-metrics.png)

For each paper, these metrics data will be displayed:

* Rating score - This is an average rating score, 10 as the highest. The number of people rated also included. Mouse over to **Rate this paper** to rate the paper.
* Views - Number of times this papers was viewed
* Comments - Number of comments
* Discussion - Number of discussion
* Collected folders - Number of folders that contain this paper
* Citation in pubmed - Citaion count from Pubmed
* Altmetric - The social media about this paper

####Authors<a name="paper-details-authors"></a>

On default, only the author names for the first two authors and the last author will be displayed. More details can be expanded by click the `arrow` on the right side.

On the expanded author panel. Includes:

* Full author names
* Author affinity
* Journal info

Click the `<` arrow to collapse the author panel.

![labii-reference-manager-paper-details-author-collapose](https://labiiblog.files.wordpress.com/2015/05/labii-reference-manager-paper-details-author-collapose.png)

![labii-reference-manager-paper-details-author-expand](https://labiiblog.files.wordpress.com/2015/05/labii-reference-manager-paper-details-author-expand.png)

####Abstract<a name="paper-details-abstract"></a>

Same to the author panel, the abstract panel can be expand or collapse by clicking `arrow` on the right side.

![labii-reference-manager-paper-details-abstract-collapse](https://labiiblog.files.wordpress.com/2015/05/labii-reference-manager-paper-details-abstract-collapse.png)

![labii-reference-manager-paper-details-abstract-expand](https://labiiblog.files.wordpress.com/2015/05/labii-reference-manager-paper-details-abstract-expand.png)

####Paper links<a name="paper-details-paper-links"></a>

![labii-reference-manager-paper-details-links](https://labiiblog.files.wordpress.com/2015/05/labii-reference-manager-paper-details-links.png)

Currently, we provides:

* Pubmed link
* Full text link
* Pubmed Center link
* PubReader link
* PDF link

The links will be hided if not available.

####Comments<a name="paper-details-comments"></a>

![labii-reference-manager-paper-details-comments](https://labiiblog.files.wordpress.com/2015/05/labii-reference-manager-paper-details-comments.png)

Short comments about this paper can be posted directly once login. For each comments, you can:

* Thumb up or thumb down a comment
* Reply the comment by clicking the comment icon
* Set as internal - to view by yourself only
* Hide my name - to not show your name
* Edit
* Delete
* Rport spam

####Discussion<a name="paper-details-discussion"></a>

![labii-reference-manager-paper-details-discussion](https://labiiblog.files.wordpress.com/2015/05/labii-reference-manager-paper-details-discussion.png)

Discussion is design for long comments or long discussion. On default, the discussion details was hided. Click the discussion title to expand.

Save edit functions was abailable for discussion:

* Rate discussion
* Comment on the discussion
* Set as internal - to view by yourself only
* Hide my name - to not show your name
* Edit
* Delete
* Rport spam

---

### Libraries

The papers can be stored in the library papers. The folders with different levels was designed so that the topic and subtopic can be chained.

The folders can be set as private or public. The public one can be viewed and followed by any one in the website, specifically designed for paper sharing.

#### Add a folder
#### Edit a folder
#### Delete a folder
#### Folder details
#### Add papers to a folder
#### View papers from a folder
#### Delete papers from a folder
#### Import papers from BibTex file
#### Import papers from Mendeley
#### Export papers to BibTex file
#### View shared folders

#### Add a folder

![labii-reference-manager-add-a-folder](https://labiiblog.files.wordpress.com/2015/05/labii-reference-manager-add-a-folder.png)

Click the "+" button next to **My Folders** to add a folder:

* Parent Folder - The new folder can be placed under any parent folder that selected
* Folder Name
* Description - Description to the folder, it is recommendated to added this field, especially for the public folders.
* Folder Color - Our system will randomly create an color for you. The Chrome is encourged to use with our website. Many HTML5 elements used in the platform are not well supported in other browsers.
* Share to public


#### Import from mendeley

1. Create an empty folder under "Libraries" panel. (Optional). You can use any folders that you already created;
2. Select a folder to store the papers from Mendeley. Click the folder;
3. On the right panel, click "Import" to show the dropdown menu. Select "Import from Mendeley".
![labii-reference-manager-import-mendeley-1.png](https://labiiblog.files.wordpress.com/2015/05/labii-reference-manager-import-mendeley-1.png)

4. Fill the mendeley username and password and submit.
![labii-reference-manager-import-mendeley-2.png](https://labiiblog.files.wordpress.com/2015/05/labii-reference-manager-import-mendeley-2.png)

5. If the username and password is correct, you will be redirect a info page shortly. An notification email will be sent once importing is finished. Close the popout windown.
![labii-reference-manager-import-mendeley-3.png](https://labiiblog.files.wordpress.com/2015/05/labii-reference-manager-import-mendeley-3.png)

6. Check your email and refresh page to see the newly imported papers.
> Note: The duplicated papers will be automatically ignored.

---

### Topics

---

### Journals
