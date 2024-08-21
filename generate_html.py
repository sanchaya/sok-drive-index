#!/usr/bin/env python3
import json

def generate_html_from_json(json_file, output_html):
    with open(json_file, 'r', encoding='utf-8') as f:
        books = json.load(f)

    books_json = json.dumps(books, ensure_ascii=False, indent=4)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SERVANTS OF KNOWLEDGE</title>
        <link rel="icon" href="public/servantsofknowledge-favicon.png" sizes="32x32" type="image/png">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
        <style>
         html, body {{
                height: 100%;
                margin: 0;
                display: flex;
                flex-direction: column;
            }}
            body {{
                font-family: Arial, sans-serif;
                font-size: 16px;
            }}
              .head{{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 10px 40px;
                background-color: #070202e3;
                color:#aaa;
                border-bottom: 2px solid #ddd;
            }}
            .head :hover {{
                color: #fff;
            }}
            .logo{{
                display: flex;
                align-items: center;
                margin-right: 20px;
                color: #fff;
            }}
            .logo img{{
                width: 30px; 
                height: 30px;
                margin-right: 10px; 
            }}
            .image-text {{
                display: flex;
                align-items: center;
                margin-right: 20px; 
                gap:5px;
            }}

           

            .nav-links {{
                display: flex;
                align-items: center;
                margin-left: auto; 
            }}

            .nav-links a {{
                margin-left: 20px; 
                text-decoration: none;
                color: #aaa;
            }}

            .nav-links a:hover {{
                color: #fff;
            }}
                   .image-text svg {{
        vertical-align: middle;
    }}
       
            .header {{
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 20px 80px;
                text-align: left;
            }}
            .header img {{
                max-height: 100px;
                margin-right: 20px;
            }}
            .header-content {{
                flex-grow: 1;
            }}
            .header-content p {{
                margin: 0;
                font-size: 16px;
                line-height: 1.5;
            }}
         
                .container {{
                display: grid;
                grid-template-columns: 20% 80%;
                grid-template-rows: 40px;
                gap: 10px;
                padding: 10px 80px;
               flex: 1;
               
               
            }}
          
            .filters {{
                overflow-y: auto;
                overflow: scroll;
                grid-column: 1 / 2;
                padding: 5px;
                border-radius: 20px;
                font-size: 16px;
                margin-bottom: 20px;
                height: calc(100vh - 300px);
               
            }}
            .filters fieldset {{
                margin-bottom: 10px;
            }}

            .filters fieldset div {{
                display: inline-block;
                margin-right: 10px;
            }}


            .filters label {{
                display: block;
                margin-bottom: 5px;
                margin-top: 10px;
            }}
            .filters input, .filters select {{
                width: 90%;
                margin-bottom: 10px;
            }}
            .filter-section {{
                margin-bottom: 20px;
                margin-top: 10px;
            }}

            .filter-section div {{
                display: flex;
                align-items: center;
                margin-bottom: 5px;
            }}

           

            .filter-section input[type="checkbox"] {{
                margin-right: 10px;
                width:15px;
            }}
           
            .search-bar {{
                grid-column: 2 / -1;
                border-radius: 20px; 
                text-align: center;
                 position: relative;
                 
            }}

            .search-bar input[type="text"] {{
                width: 50%;
                padding: 8px;
                font-size: 16px;
                border: 1px solid #ccc;
                border-radius: 20px; /* Match the parent's border-radius */
            }}

            .search-bar input[type="text"]:focus {{
                outline: none;
                border-color: #aaa;
            }}
            .books-container {{
               grid-column: 2 / -1;
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
                gap: 10px;
                margin-bottom:20px;
                overflow-y: auto;
                padding: 80px;
               margin-top: 20px;
            height: calc(100vh - 400px);
            }}
        .view-options {{
            position: absolute;
            right: 200px;
            top: 30px;
        }}
        .view-options i {{
            margin-left: 10px;
            cursor: pointer;
            font-size: 20px;
        }}
          
            .book {{
                position: relative;
                overflow: visible;
                margin-bottom: 10px;
                padding: 0;
                cursor: pointer;
            }}
            .book:hover .details-tooltip {{
                display: flex;
            }}
            .thumbnail {{
                position: relative;
                overflow: hidden;
            }}
            .thumbnail img {{
                max-width: 100%;
                display: block;
                height: auto;
                width: 120px; 
                height: 180px;
                transition: transform 0.2s;
            }}
            .book-title {{
                text-align: left;
                padding: 10px;
                font-size: 16px;
               
               
            }}
            .details-tooltip {{
                position: absolute;
                top: -90px; 
                left: calc(-20% - 10px); 
                transform: translateX(0%);
                width: 300px; 
                background-color: rgba(255, 255, 255, 0.95);
                color: black;
                display: none;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                opacity: 1;
                padding: 20px;
                box-sizing: border-box;
                z-index: 9999; 
                border: 1px solid #090909;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            }}
            .details {{
                text-align: left;
            }}
            .details h3 {{
                margin: 0;
            }}
            .details p {{
                margin: 5px 0;
            }}
            .details-tooltip .read-icon {{
            position: absolute;
            right: 0;
            bottom: 0;
        }}
        
.list-view .books-container {{
    display: block; 
    padding: 0;
    height: auto; 
    width: 100%;
    overflow: visible;
}}

.list-view .book {{
    display: flex;
    align-items: flex-start;
    
    border: 1px solid #ddd;
    border-radius: 10px;
    background-color: #fff;
    margin-bottom: 20px;
    padding: 10px;
    width: 100%; 
}}

.list-view .thumbnail {{
    width: 120px; 
    height: auto;
    margin-right: 20px; 
    flex-shrink: 0;
}}

.list-view .thumbnail img {{
    width: 100%;
    height: auto;
    margin-right: 20px;
}}
.list-view .book-title {{
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 5px;
}}

.list-view .details {{
    flex-grow: 1;
    font-size: 16px;
    text-align: left; 
}}
.list-view .details-tooltip {{
    display: none;
}}
            .clear {{
                clear: both;
            }}
              #search-books{{
                margin-top: 20px;
            }}
            .footer {{
                
                grid-column: 1 / -1;
                background-color: #070202e3;
                text-align: center;
                padding: 10px 5px;
                border-radius: 5px;
                color: #fff;
                margin-top: 20px;
                position: fixed;
                bottom: 0;
                width: 100%;
            }}
             .show-more {{
            cursor: pointer;
            color: black;
         
        }}
         #clear-filters-button {{
            margin-bottom: 50px; 
        }}
         #iframeContainer {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            justify-content: center;
            align-items: center;
            overflow: hidden;
            z-index: 1000;
        }}

        #iframe {{
            width: 80%;
            height: 80%;
            border: none;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        }}

        #closeBtn {{
            position: absolute;
            top: 10px;
            right: 20px;
            font-size: 24px;
            color: white;
            cursor: pointer;
            z-index: 1001;
        }}
        .fullscreen-modal {{
            display: none; 
            position: fixed;
            z-index: 2; /* Sit on top */
            left: 50%; 
            top: 50%; 
            transform: translate(-50%, -50%);
            width: 30%;
            height: 30%; 
            background-color: rgba(0, 0, 0, 0.8); 
            overflow: hidden;
            display: flex; 
            justify-content: center; 
            align-items: center; 
        }}

        .fullscreen-image {{
            height: 100%; 
            width: auto; 
            flex: 1; 
            object-fit: cover; 
            
        }}
              
        .modal {{
            display: none; 
            position: fixed; 
            z-index: 1; 
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto; 
            background-color: rgba(0,0,0,0.5);
            padding-top: 15px;
        }}

        /* Modal content box */
        .modal-content {{
            background-color: white;
            margin: 5% auto;
            padding: 20px;
            border: 1px solid #888;
            width: 60%;
            max-width: 600px; 
            box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
            text-align: center;
        }}
        .justified-content {{
            text-align: justify;
            line-height: 1.5; 
            white-space: pre-wrap; 
            padding: 0 20px;
        }}
        .image-container {{
            text-align: center; 
            margin-bottom: 20px; 
        }}

        .gandhi-image {{
            max-width: 100%; 
            height: auto; 
            display: inline-block; 
        }}

        /* Close button */
        .close {{
            color: #aaa;
            float: right;
            font-size: 28px;
            font-weight: bold;
        }}

        .close:hover,
        .close:focus {{
            color: black;
            text-decoration: none;
            cursor: pointer;
        }}
        @media (max-width: 600px) {{
            #iframe {{
                width: 85%;
                height: 85%;
            }}
        }}
        
        </style>
    </head>
    <body>
    <div id="gandhiImageModal" class="fullscreen-modal">
            <img src="public/gandhi.jpeg" alt="Gandhi" class="fullscreen-image">
            <img src="public/gandhiknowledgetrust.jpeg" alt="Gandhi Knowledge Trust" class="fullscreen-image">
        </div>
    <div class="head">
            <div class="logo">
                <img src="public/servants of knowledge.png" alt="servantsofknowledge">
                <span>#SERVANTSOFKNOWLEDGE</span>
            </div>
            <div class="image-text">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-book" viewBox="0 0 16 16">
                    <path d="M1 2.828c.885-.37 2.154-.769 3.388-.893 1.33-.134 2.458.063 3.112.752v9.746c-.935-.53-2.12-.603-3.213-.493-1.18.12-2.37.461-3.287.811zm7.5-.141c.654-.689 1.782-.886 3.112-.752 1.234.124 2.503.523 3.388.893v9.923c-.918-.35-2.107-.692-3.287-.81-1.094-.111-2.278-.039-3.213.492zM8 1.783C7.015.936 5.587.81 4.287.94c-1.514.153-3.042.672-3.994 1.105A.5.5 0 0 0 0 2.5v11a.5.5 0 0 0 .707.455c.882-.4 2.303-.881 3.68-1.02 1.409-.142 2.59.087 3.223.877a.5.5 0 0 0 .78 0c.633-.79 1.814-1.019 3.222-.877 1.378.139 2.8.62 3.681 1.02A.5.5 0 0 0 16 13.5v-11a.5.5 0 0 0-.293-.455c-.952-.433-2.48-.952-3.994-1.105C10.413.809 8.985.936 8 1.783"/>
                  </svg>
                <span>BOOKS</span>
            </div>
            <div class="image-text">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-camera-video" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M0 5a2 2 0 0 1 2-2h7.5a2 2 0 0 1 1.983 1.738l3.11-1.382A1 1 0 0 1 16 4.269v7.462a1 1 0 0 1-1.406.913l-3.111-1.382A2 2 0 0 1 9.5 13H2a2 2 0 0 1-2-2zm11.5 5.175 3.5 1.556V4.269l-3.5 1.556zM2 4a1 1 0 0 0-1 1v6a1 1 0 0 0 1 1h7.5a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1z"/>
                  </svg>
                <span>VIDEO</span>
            </div>
            <div class="image-text">
                 <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-earmark-music" viewBox="0 0 16 16">
                    <path d="M11 6.64a1 1 0 0 0-1.243-.97l-1 .25A1 1 0 0 0 8 6.89v4.306A2.6 2.6 0 0 0 7 11c-.5 0-.974.134-1.338.377-.36.24-.662.628-.662 1.123s.301.883.662 1.123c.364.243.839.377 1.338.377s.974-.134 1.338-.377c.36-.24.662-.628.662-1.123V8.89l2-.5z"/>
                    <path d="M14 14V4.5L9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2M9.5 3A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h5.5z"/>
                  </svg>
                <span>AUDIO</span>
            </div>
            <div class="nav-links">
                <a href="#aboutus" id="openAboutUs">About Us</a>
                <a href="#contactus" id="openGandhiTrust">Gandhi Library Knowledge Trust</a>
            </div>
        </div>
        <!-- About Us Modal -->
<div id="aboutUsModal" class="modal">
    <div class="modal-content">
        <span class="close" id="closeAboutUs">&times;</span>
        <h2>About Us</h2>
        <div class="justified-content">
“All India Gandhi Library to advance access to knowledge and spread the Mahatma’s message”

This digital repository is the result of a collaboration between Karnataka Gandhi Smaraka Nidhi and the Servants of Knowledge, a non-profit Section 8 association dedicated to advancing access to knowledge. The entire library was digitised in only 3 months and additional contributions were made by the Telangana Gandhi Smaraka Nidhi and the Andrapradesh Gandhi Smaraka Nidhi.

The library includes the volumes of Collected Works of Mahatma Gandhi as well as hundreds of other Gandhi resources including Harijan, Young India, Indian Opinion, many Navijavan Trust pamphlets, the Pyarlel biographies, the Desai diaries and much more. In addition, the repository includes extensive collections of the works of Nehru and Ambedkar, the Sardar Patel correspondence, and works by numerous others such as Netaji Subhas Chandra Bose and Sarvepalli Radhakrishnan. The multimedia collection also includes 129 audio files of Mahatma Gandhi speaking on All India Radio. The collection includes works in 12 languages.

Gandhi Bhavan already makes 1,272 public domain works available to the general public at <a href="https://archive.org/details/GandhiBhavan" target="_blank">https://archive.org/details/GandhiBhavan</a>. The presentation of the digital library to Gandhi organisations across the country allows those groups to access a much wider collection of works for noncommercial uses allowed by the Copyright Act of India, including access by the blind, research use, and uses in the course of instruction. In addition to the digital collection, the organisations are being furnished with an extensive treatise on the permitted uses of materials by public libraries.
        </div>
    </div>
</div>

<!-- Gandhi Trust Modal -->
<div id="gandhiTrustModal" class="modal">
    <div class="modal-content">
        <span class="close" id="closeGandhiTrust">&times;</span>
        <h2>GANDHI LIBRARY KNOWLEDGE TRUST</h2>
        <p> (VERSION 1.1)</p>
        <div class="image-container">
            <img src="public/gandhi.jpeg" alt="Gandhi" class="gandhi-image">
        </div>
        <div> 
            <p>NOTICE AND ACKNOWLEDGEMENT</p>
            <p>OF TRUSTEESHIP</p>
        </div>
        <div class="justified-content">
By access and using the enclosed library of knowledge containing the full digitisation of the library of Gandhi Bhavan (Bengaluru), you do hereby agree and affirm that these materials shall ONLY be used for the noncommercial purposes of research, in the course of instruction, accessibility by the visually impaired and other uses AS PERMITTED UNDER THE LAWS OF INDIA. You must inform any other users of these materials of these conditions.
        </div>
        <div>
            <p><b>“SCANNING IS THE NEW SPINNING”</b></p><p><b>JAI GYAN</b></p>
        </div>
    </div>
</div>
     <div class="header">
            <img src="public/gandhi.jpeg" alt="Gandhi">
            <div class="header-content">
                <p><strong>#SERVANTSOFKNOWLEDGE Scanning Is The New Spinning</strong></p>
                <br>
                <p>All India Gandhi Library v1.0
<br>
The library includes the volumes of Collected Works of Mahatma Gandhi as well as hundreds of other Gandhi resources including Harijan, Young India, Indian Opinion, 
many Nava jeevan Trust pamphlets, the Pyarelal biographies, the Desai diaries and much more.
In addition, the repository includes extensive collections of the works of Nehru and Ambedkar, the Sardar Patel correspondence, and works by numerous others
such as Netaji Subhas Chandra Bose and Sarvepalli Radhakrishnan. The multimedia collection also includes 129 audio files of Mahatma Gandhi speaking on All India Radio.
The collection includes works in 12 languages.</p>
                
            </div>
        </div>
         <div class="container">
            <div class="filters">
    <h3>Filters</h3>

 
    <div class="filter-section" id="filter-section-year">
        <h3>Year</h3>
        
        <button class="show-more" onclick="toggleYearFilters()">Show more</button>
        
    </div>

    <div class="filter-section" id="filter-section-author">
        <h3>Author</h3>
       
     
        <button class="show-more" onclick="toggleAuthorFilters()">Show more</button>
    </div>

    <div class="filter-section" id="filter-section-lang">
        <h3>Language</h3>
       
        
        <button class="show-more" onclick="toggleLanguageFilters()">Show more</button>
    </div>

    <div class="filter-section" id="filter-section-sub">
        <h3>Subject</h3>
       
       
        <button class="show-more" onclick="toggleSubjectFilters()">Show more</button>
    </div>

    <div class="filter-section" id="filter-section-publisher">
        <h3>Publisher</h3>
       
      
        <button class="show-more" onclick="togglePublisherFilters()">Show more</button>
    </div>

    <button id="clear-filters-button" onclick="clearFilters()">Clear Filters</button>
</div>


            <div class="search-bar">
            <input type="text" id="search-books" placeholder="Search..." >
            <div class="view-options">
                <i class="fas fa-th-large" id="grid-view-icon" onclick="setGridView()"></i>
                <i class="fas fa-list" id="list-view-icon" onclick="setListView()"></i>
            </div>
            </div>

            <div class="books-container" id="books"></div>
           <div id="iframeContainer">
                <iframe id="iframe" src="" frameborder="0"></iframe>
                <span id="closeBtn">&times;</span>
            </div>
           
        </div>
             <div class="footer">
                 #ServantsOfKnowledge - Scanning Is The New Spinning 
            </div>
        <script>
              function setGridView() {{
                console.log('setgrid');
                document.querySelector('.books-container').classList.remove('list-view');
                document.querySelector('.books-container').style.display = 'grid';
                booksLoaded=0;
                loadBooksInView('grid'); 
                console.log("Switched to grid view");
        }}

        function setListView() {{
            console.log('setlist');
            document.querySelector('.books-container').classList.add('list-view');
    document.querySelector('.books-container').style.display = 'block'; 
    booksLoaded=0;
    loadBooksInView('list');
                console.log("Switched to list view");
        }}
                    const booksData = {books_json};
let booksLoaded = 0;
const booksPerBatch = 25; // Number of books to load per batch
const totalBooks = booksData.length;

let count=0;
function loadMoreBooks(view) {{
    console.log('loadmore');
    
    const booksContainer = document.getElementById('books');
    const iframeContainer = document.getElementById('iframeContainer');
    const iframe = document.getElementById('iframe');
    const closeBtn = document.getElementById('closeBtn');
    let start = booksLoaded;
    let end = Math.min(booksLoaded + booksPerBatch, totalBooks);
   
    for (let i = start; i < end ; i++) {{
        const book = booksData[i];
        const bookDiv = document.createElement('div');
        count++;
        if (view === 'grid') {{
            bookDiv.className = 'book grid-view-item';  // Class for grid view

            // Create thumbnail for grid view
            const thumbnail = document.createElement('div');
            thumbnail.className = 'thumbnail';
            const img = document.createElement('img');
            if (book.thumbnail_url!=null) {{
            img.src = book.thumbnail_url;
            thumbnail.appendChild(img);
            }}
            const title = document.createElement('div');
            title.className = 'book-title';
            title.textContent = book.title;
       

            // Add tooltip for grid view
          const detailsTooltip = document.createElement('div');
                        detailsTooltip.className = 'details-tooltip';
                        const details = document.createElement('div');
                        details.className = 'details';
                        details.innerHTML = `
                            <h3>${{book.title}}</h3>
                            <p><strong>Author:</strong> ${{book.creators.join(', ')}}</p>
                            <p><strong>Publisher:</strong> ${{book.publisher}}</p>
                            <p><strong>Language:</strong> ${{book.language}}</p>
                            <p><strong>Year:</strong> ${{book.year}}</p>
                            <p><strong>Subject:</strong> ${{book.subject}}</p>
                            <img src="public/book.jpg" alt="Read Book" height="50" width="50" class="read-icon">
                        `;
                        detailsTooltip.appendChild(details);

              bookDiv.appendChild(thumbnail);
                        bookDiv.appendChild(title);
                        bookDiv.appendChild(detailsTooltip);
                        detailsTooltip.addEventListener('click', () => {{
                            iframe.src = book.pdf_url;
                            iframeContainer.style.display = 'flex';
                            document.body.style.overflow = 'hidden';  // Disable scrolling
                        }});
       

            }}
            else if (view === 'list') {{
            bookDiv.className = 'book list-view-item';  // Class for list view

            // Create clickable thumbnail
            const thumbnail = document.createElement('div');
            thumbnail.className = 'thumbnail';
            const img = document.createElement('img');
           if (book.thumbnail_url!=null) {{
            img.src = book.thumbnail_url;
            thumbnail.appendChild(img);
            }}
            else{{
                const title = document.createElement('div');
                title.className = 'book-title';
                title.textContent = book.title;
                thumbnail.appendChild(title);
            }}
                
                    

        

        
            // Add event listener to open PDF in iframe on click
        thumbnail.addEventListener('click', () => {{
            iframe.src = book.pdf_url;
            iframeContainer.style.display = 'flex';
            document.body.style.overflow = 'hidden';
        }});

        bookDiv.appendChild(thumbnail);
            // Create book details for list view
            const details = document.createElement('div');
            details.className = 'details';
            details.innerHTML = `
                <h3>${{book.title}}</h3>
                <p><strong>Author:</strong> ${{book.creators.join(', ')}}</p>
                <p><strong>Publisher:</strong> ${{book.publisher}}</p>
                <p><strong>Year:</strong> ${{book.year}}</p>
                <p><strong>Language:</strong> ${{book.language}}</p>
                <p><strong>Subject:</strong> ${{book.subject}}</p>
            `;
           
           
           bookDiv.appendChild(details);
                       
                     
        }}

        booksContainer.appendChild(bookDiv);
       
    }}
 closeBtn.addEventListener('click', () => {{
                        iframe.src = '';  // Clear the iframe source
                        iframeContainer.style.display = 'none';
                        document.body.style.overflow = 'auto';  // Enable scrolling
        }});
    booksLoaded += (end - start); // Increment booksLoaded by the number of books loaded

// If there are more books to load, create observer for the last book
if (booksLoaded < totalBooks) {{
    
    createObserver(view);
}}

}}

function createObserver(view) {{
    console.log('obs');
    const options = {{
        root: document.getElementById('books-container'),  // Use books container for scroll
        rootMargin: '0px',
        threshold: 1.0
    }};

   const  observer = new IntersectionObserver((entries, observer) => {{
        console.log('intersect');
        console.log(count);
        entries.forEach(entry => {{
            if (entry.isIntersecting) {{
                observer.unobserve(entry.target);  // Stop observing the last book
                loadMoreBooks(view);  // Load more books based on the view
            }}
        }});
    }}, options);
    const lastBook = document.querySelector('.book:last-child');
    if (lastBook) {{
        observer.observe(lastBook);  // Observe the last book in the container
    }}
    
}}
function observeLastBook() {{
    console.log('obslast');
    if (observer) {{
        console.log('obsif');
        const lastBook = document.querySelector('.book:last-child');
        if (lastBook) {{
            console.log('last');
            observer.observe(lastBook);
        }}
    }}
}}
function loadBooksInView(view) {{
    console.log('main');
    const booksContainer = document.getElementById('books');
    booksContainer.innerHTML = '';
    booksLoaded = 0;  // Reset loaded books count
    loadMoreBooks(view);  // Start loading books based on the view
    console.log(count);
}}
                    
            
               function clearFilters() {{
                console.log('clear');
                document.getElementById('search-books').value = '';
                // Clear other filter inputs here
                 document.querySelectorAll('.filters input[type="checkbox"]').forEach(checkbox => {{
                    checkbox.checked = false;
                }});
                const isListView = document.querySelector('.books-container').classList.contains('list-view');

            if (isListView) {{
                booksLoaded=0;
                loadBooksInView('list');
            }} else {{
                booksLoaded=0;
                loadBooksInView('grid');

            }}
            }}
                // Initialize filter checkboxes
                    function initializeFilters() {{
                    
                        const filterSectionYear = document.getElementById('filter-section-year');
                        const uniqueYears = [...new Set(booksData.map(book => book.year).filter(year => year !=="N/A" ))];
                        uniqueYears.sort((a,b) => b - a);
                        uniqueYears.slice(0, Math.min(5, uniqueYears.length)).forEach(year => {{
                            const div = document.createElement('div');
                            const input = document.createElement('input');
                            input.type = 'checkbox';
                            input.value = year;
                            input.className = 'filter-checkbox';
                            input.id = `filter-year-${{year}}`;
                            input.addEventListener('change', applyFilters);

                            const label = document.createElement('label');
                            label.htmlFor = `filter-year-${{year}}`;
                            label.textContent = year;

                            div.appendChild(input);
                            div.appendChild(label);
                            filterSectionYear.insertBefore(div, filterSectionYear.querySelector('.show-more'));

                            
                        }});

                         
                        const filterSectionAuthor = document.getElementById('filter-section-author');
                            const uniqueAuthors = [...new Set(booksData.flatMap(book => {{
                                if (Array.isArray(book.creators)) {{
                                    return book.creators.map(author => author.trim());
                                }} else {{
                                    return [];
                                }}
                            }}))];
                      
                       uniqueAuthors.slice(0, Math.min(5,uniqueAuthors.length)).forEach(author => {{
                        const div = document.createElement('div');
                        const input = document.createElement('input');
                        input.type = 'checkbox';
                        input.value = author;
                        input.className = 'filter-checkbox';
                        input.id = `filter-author-${{author}}`;
                        input.addEventListener('change', applyFilters);

                        const label = document.createElement('label');
                        label.htmlFor = `filter-author-${{author}}`;
                        label.textContent = author;

                        div.appendChild(input);
                        div.appendChild(label);
                            filterSectionAuthor.insertBefore(div, filterSectionAuthor.querySelector('.show-more'));
                            }});

                        const filterSectionLanguage = document.getElementById('filter-section-lang');
                        const uniqueLanguages = [...new Set(booksData.map(book => book.language).filter(language => language !=="N/A"))];
                       
                        uniqueLanguages.slice(0, Math.min(5,uniqueLanguages.length)).forEach(language => {{
                            const div = document.createElement('div');
                            const input = document.createElement('input');
                            input.type = 'checkbox';
                            input.value = language;
                            input.className = 'filter-checkbox';
                            input.id = `filter-language-${{language}}`;
                            input.addEventListener('change', applyFilters);

                            const label = document.createElement('label');
                            label.htmlFor = `filter-language-${{language}}`;
                            label.textContent = language;

                            div.appendChild(input);
                            div.appendChild(label);
                            filterSectionLanguage.insertBefore(div, filterSectionLanguage.querySelector('.show-more'));
                            }});

                         const filterSectionPublisher = document.getElementById('filter-section-publisher');
                        const uniquePublishers = [...new Set(booksData.map(book => book.publisher).filter(publisher => publisher !== "N/A"))];
                       
                        uniquePublishers.slice(0, Math.min(5, uniquePublishers.length)).forEach(publisher => {{
                            const div = document.createElement('div');
                            const input = document.createElement('input');
                            input.type = 'checkbox';
                            input.value = publisher;
                            input.className = 'filter-checkbox';
                            input.id = `filter-publisher-${{publisher}}`;
                            input.addEventListener('change', applyFilters);

                            const label = document.createElement('label');
                            label.htmlFor = `filter-publisher-${{publisher}}`;
                            label.textContent = publisher;

                            div.appendChild(input);
                            div.appendChild(label);
                            filterSectionPublisher.insertBefore(div, filterSectionPublisher.querySelector('.show-more'));
                            }});

                         const filterSectionSubject = document.getElementById('filter-section-sub');
                       const uniqueSubjects = [...new Set(booksData.flatMap(book => {{
                            return book.subject.split(';').map(subject => subject.trim()).filter(subject => subject !== "N/A");
                        }}))];

                        // Generate checkboxes for unique subjects, show all if less than 5
                        uniqueSubjects.slice(0, Math.min(5, uniqueSubjects.length)).forEach(subject => {{
                            const div = document.createElement('div');
                            const input = document.createElement('input');
                            input.type = 'checkbox';
                            input.value = subject;
                            input.className = 'filter-checkbox';
                            input.id = `filter-subject-${{subject}}`;
                            input.addEventListener('change', applyFilters);

                            const label = document.createElement('label');
                            label.htmlFor = `filter-subject-${{subject}}`;
                            label.textContent = subject;

                            div.appendChild(input);
                            div.appendChild(label);
                            filterSectionSubject.insertBefore(div, filterSectionSubject.querySelector('.show-more'));
                        }});
                    }}

                   

                     let showAllYears = false;

                    function toggleYearFilters() {{
                        const filterSectionYear = document.getElementById('filter-section-year');
                        filterSectionYear.innerHTML = '<h3>Year</h3>';
                        const uniqueYears = [...new Set(booksData.map(book => book.year).filter(year => year!=="N/A"))];
                        uniqueYears.sort((a,b) => b - a);
                        if (showAllYears) {{
                            uniqueYears.slice(0, Math.min(5,uniqueYears.length)).forEach(year => {{
                                const div = document.createElement('div');
                                const input = document.createElement('input');
                                input.type = 'checkbox';
                                input.value = year;
                                input.className = 'filter-checkbox';
                                input.id = `filter-year-${{year}}`;
                                input.addEventListener('change', applyFilters);

                                const label = document.createElement('label');
                                label.htmlFor = `filter-year-${{year}}`;
                                label.textContent = year;

                                div.appendChild(input);
                                div.appendChild(label);
                                filterSectionYear.insertBefore(div, filterSectionYear.querySelector('.show-more'));
                            }});
                            filterSectionYear.appendChild(createToggleButton('Show More', toggleYearFilters));
                        }} else {{
                            uniqueYears.forEach(year => {{
                                const div = document.createElement('div');
                                const input = document.createElement('input');
                                input.type = 'checkbox';
                                input.value = year;
                                input.className = 'filter-checkbox';
                                input.id = `filter-year-${{year}}`;
                                input.addEventListener('change', applyFilters);

                                const label = document.createElement('label');
                                label.htmlFor = `filter-year-${{year}}`;
                                label.textContent = year;

                                div.appendChild(input);
                                div.appendChild(label);
                                filterSectionYear.insertBefore(div, filterSectionYear.querySelector('.show-more'));
                            }});
                            filterSectionYear.appendChild(createToggleButton('Hide', toggleYearFilters));
                        }}
                        showAllYears = !showAllYears;
                    }}

                    let showAllAuthors = false;

                    function toggleAuthorFilters() {{
                        const filterSectionAuthor = document.getElementById('filter-section-author');
                        filterSectionAuthor.innerHTML = '<h3>Author</h3>';
                        const uniqueAuthors = [...new Set(booksData.flatMap(book => {{
                            if (Array.isArray(book.creators)) {{
                                return book.creators.map(author => author.trim());
                            }} else {{
                                return [];
                            }}
                        }}))];
                        
                        if (showAllAuthors) {{
                            uniqueAuthors.slice(0, Math.min(5,uniqueAuthors.length)).forEach(author => {{
                                const div = document.createElement('div');
                                const input = document.createElement('input');
                                input.type = 'checkbox';
                                input.value = author;
                                input.className = 'filter-checkbox';
                                input.id = `filter-author-${{author}}`;
                                input.addEventListener('change', applyFilters);

                                const label = document.createElement('label');
                                label.htmlFor = `filter-author-${{author}}`;
                                label.textContent = author;

                                div.appendChild(input);
                                div.appendChild(label);
                                filterSectionAuthor.insertBefore(div, filterSectionAuthor.querySelector('.show-more'));
                            }});
                            filterSectionAuthor.appendChild(createToggleButton('Show More', toggleAuthorFilters));
                        }}else {{
                            uniqueAuthors.forEach(author => {{
                                const div = document.createElement('div');
                                const input = document.createElement('input');
                                input.type = 'checkbox';
                                input.value = author;
                                input.className = 'filter-checkbox';
                                input.id = `filter-author-${{author}}`;
                                input.addEventListener('change', applyFilters);

                                const label = document.createElement('label');
                                label.htmlFor = `filter-author-${{author}}`;
                                label.textContent = author;

                                div.appendChild(input);
                                div.appendChild(label);
                                filterSectionAuthor.insertBefore(div, filterSectionAuthor.querySelector('.show-more'));
                            }});
                            filterSectionAuthor.appendChild(createToggleButton('Hide', toggleAuthorFilters));
                        }}
                        showAllAuthors = !showAllAuthors;
                    }}

                    let showAllPublishers = false;

                    function togglePublisherFilters() {{
                        const filterSectionPublisher = document.getElementById('filter-section-publisher');
                        filterSectionPublisher.innerHTML = '<h3>Publisher</h3>';
                        const uniquePublishers = [...new Set(booksData.map(book => book.publisher).filter(publisher => publisher !== "N/A"))];
                        
                        if (showAllPublishers) {{
                            uniquePublishers.slice(0, Math.min(5,uniquePublishers.length)).forEach(publisher => {{
                                const div = document.createElement('div');
                                const input = document.createElement('input');
                                input.type = 'checkbox';
                                input.value = publisher;
                                input.className = 'filter-checkbox';
                                input.id = `filter-publisher-${{publisher}}`;
                                input.addEventListener('change', applyFilters);

                                const label = document.createElement('label');
                                label.htmlFor = `filter-publisher-${{publisher}}`;
                                label.textContent = publisher;

                                div.appendChild(input);
                                div.appendChild(label);
                                filterSectionPublisher.appendChild(div);
                            }});
                            filterSectionPublisher.appendChild(createToggleButton('Show More', togglePublisherFilters));
                        }} else {{
                            uniquePublishers.forEach(publisher => {{
                                const div = document.createElement('div');
                                const input = document.createElement('input');
                                input.type = 'checkbox';
                                input.value = publisher;
                                input.className = 'filter-checkbox';
                                input.id = `filter-publisher-${{publisher}}`;
                                input.addEventListener('change', applyFilters);

                                const label = document.createElement('label');
                                label.htmlFor = `filter-publisher-${{publisher}}`;
                                label.textContent = publisher;

                                div.appendChild(input);
                                div.appendChild(label);
                                filterSectionPublisher.appendChild(div);
                            }});
                            filterSectionPublisher.appendChild(createToggleButton('Hide', togglePublisherFilters));
                        }}
                        showAllPublishers = !showAllPublishers;
                    }}

                    let showAllSubjects = false;

                    function toggleSubjectFilters() {{
                        const filterSectionSubject = document.getElementById('filter-section-sub');
                        filterSectionSubject.innerHTML = '<h3>Subject</h3>';
                        const uniqueSubjects = [...new Set(booksData.flatMap(book => book.subject.split(';').map(subject => subject.trim())).filter(subject => subject !== "N/A"))];
                        
                        if (showAllSubjects) {{
                            uniqueSubjects.slice(0, Math.min(5, uniqueSubjects.length)).forEach(subject => {{
                                const div = document.createElement('div');
                                const input = document.createElement('input');
                                input.type = 'checkbox';
                                input.value = subject;
                                input.className = 'filter-checkbox';
                                input.id = `filter-subject-${{subject}}`;
                                input.addEventListener('change', applyFilters);

                                const label = document.createElement('label');
                                label.htmlFor = `filter-subject-${{subject}}`;
                                label.textContent = subject;

                                div.appendChild(input);
                                div.appendChild(label);
                                filterSectionSubject.appendChild(div);
                            }});
                            filterSectionSubject.appendChild(createToggleButton('Show More', toggleSubjectFilters));
                        }} else {{
                            uniqueSubjects.forEach(subject => {{
                                const div = document.createElement('div');
                                const input = document.createElement('input');
                                input.type = 'checkbox';
                                input.value = subject;
                                input.className = 'filter-checkbox';
                                input.id = `filter-subject-${{subject}}`;
                                input.addEventListener('change', applyFilters);

                                const label = document.createElement('label');
                                label.htmlFor = `filter-subject-${{subject}}`;
                                label.textContent = subject;

                                div.appendChild(input);
                                div.appendChild(label);
                                filterSectionSubject.appendChild(div);
                            }});
                            filterSectionSubject.appendChild(createToggleButton('Hide', toggleSubjectFilters));
                        }}
                        showAllSubjects = !showAllSubjects;
                    }}

                        let showAllLanguages = false;

                        function toggleLanguageFilters() {{
                            const filterSectionLanguage = document.getElementById('filter-section-lang');
                            filterSectionLanguage.innerHTML = '<h3>Language</h3>';
                            const uniqueLanguages = [...new Set(booksData.map(book => book.language).filter(language => language !== "N/A"))];
                            
                            if (showAllLanguages) {{
                                uniqueLanguages.slice(0, Math.min(5, uniqueLanguages.length)).forEach(language => {{
                                    const div = document.createElement('div');
                                    const input = document.createElement('input');
                                    input.type = 'checkbox';
                                    input.value = language;
                                    input.className = 'filter-checkbox';
                                    input.id = `filter-language-${{language}}`;
                                    input.addEventListener('change', applyFilters);

                                    const label = document.createElement('label');
                                    label.htmlFor = `filter-language-${{language}}`;
                                    label.textContent = language;

                                    div.appendChild(input);
                                    div.appendChild(label);
                                    filterSectionLanguage.appendChild(div);
                                }});
                                filterSectionLanguage.appendChild(createToggleButton('Show More', toggleLanguageFilters));
                            }}else {{
                                uniqueLanguages.forEach(language => {{
                                    const div = document.createElement('div');
                                    const input = document.createElement('input');
                                    input.type = 'checkbox';
                                    input.value = language;
                                    input.className = 'filter-checkbox';
                                    input.id = `filter-language-${{language}}`;
                                    input.addEventListener('change', applyFilters);

                                    const label = document.createElement('label');
                                    label.htmlFor = `filter-language-${{language}}`;
                                    label.textContent = language;

                                    div.appendChild(input);
                                    div.appendChild(label);
                                    filterSectionLanguage.appendChild(div);
                                }});
                                filterSectionLanguage.appendChild(createToggleButton('Hide', toggleLanguageFilters));
                            }}
                            showAllLanguages = !showAllLanguages;
                        }}


                   function createToggleButton(text, toggleFunction) {{
                    const button = document.createElement('button');
                    button.className = 'show-more';
                    button.textContent = text;
                    button.onclick = toggleFunction;
                    return button;
                }}

                  
                   
                    function applyFilters() {{
                    const searchInput = document.getElementById('search-books').value.toLowerCase();

                    // Get all checked filters
                    const checkedFilters = Array.from(document.querySelectorAll('.filter-checkbox:checked'));
                    
                    // Extract checked values for each filter type
                    const checkedYears = Array.from(document.querySelectorAll('#filter-section-year .filter-checkbox:checked')).map(checkbox => checkbox.value);
                    const checkedAuthors = Array.from(document.querySelectorAll('#filter-section-author .filter-checkbox:checked')).map(checkbox => checkbox.value);
                    const checkedLanguages = Array.from(document.querySelectorAll('#filter-section-lang .filter-checkbox:checked')).map(checkbox => checkbox.value);
                    const checkedPublishers = Array.from(document.querySelectorAll('#filter-section-publisher .filter-checkbox:checked')).map(checkbox => checkbox.value);
                    const checkedSubjects = Array.from(document.querySelectorAll('#filter-section-sub .filter-checkbox:checked')).map(checkbox => checkbox.value);

                    // Filter books based on search input and checked filters
                    const filteredBooks = booksData.filter(book => {{
                        const matchesSearch = book.title.toLowerCase().includes(searchInput) ||
                            book.creators.some(creator => creator.toLowerCase().includes(searchInput)) ||
                            book.publisher.toLowerCase().includes(searchInput) ||
                            book.language.toLowerCase().includes(searchInput) ||
                            book.subject.toLowerCase().includes(searchInput);

                        const matchesYear = checkedYears.length === 0 || checkedYears.includes(book.year);
                        const matchesAuthor = checkedAuthors.length === 0 || book.creators.some(creator => checkedAuthors.includes(creator.trim()));
                        const matchesLanguage = checkedLanguages.length === 0 || checkedLanguages.includes(book.language);
                        const matchesPublisher = checkedPublishers.length === 0 || checkedPublishers.includes(book.publisher);
                        const matchesSubject = checkedSubjects.length === 0 || checkedSubjects.some(subject => book.subject.split(';').map(s => s.trim()).includes(subject));

                        return matchesSearch && matchesYear && matchesAuthor && matchesLanguage && matchesPublisher && matchesSubject;
                    }});
                    const isListView = document.querySelector('.books-container').classList.contains('list-view');

                   if (isListView) {{
                        
                            loadListView(filteredBooks);
                    }} else {{
                        console.log('gridview filter');
                        loadGridView(filteredBooks);
                
                    }}
                    }}

                    function loadGridView(filteredBooks){{
                    // Update the books display
                    const booksContainer = document.getElementById('books');
                     const iframeContainer = document.getElementById('iframeContainer');
                    const iframe = document.getElementById('iframe');
                    const closeBtn = document.getElementById('closeBtn');
                    booksContainer.innerHTML = '';
                    filteredBooks.forEach(book => {{
                        const bookDiv = document.createElement('div');
                        bookDiv.className = 'book';

                        const thumbnail = document.createElement('div');
                        thumbnail.className = 'thumbnail';
                        const img = document.createElement('img');
                        
                           if (book.thumbnail_url!=null) {{
                            img.src = book.thumbnail_url;
                            thumbnail.appendChild(img);
                        }}

                        const title = document.createElement('div');
                        title.className = 'book-title';
                        title.textContent = book.title;

                        const detailsTooltip = document.createElement('div');
                        detailsTooltip.className = 'details-tooltip';
                        const details = document.createElement('div');
                        details.className = 'details';
                        details.innerHTML = `
                            <h3>${{book.title}}</h3>
                            <p><strong>Author:</strong> ${{book.creators.join(', ')}}</p>
                            <p><strong>Publisher:</strong> ${{book.publisher}}</p>
                            <p><strong>Language:</strong> ${{book.language}}</p>
                            <p><strong>Year:</strong> ${{book.year}}</p>
                            <p><strong>Subject:</strong> ${{book.subject}}</p>
                            <img src="public/book.jpg" alt="Read Book" height="50" width="50" class="read-icon">
                        `;
                        detailsTooltip.appendChild(details);

                        bookDiv.appendChild(thumbnail);
                        bookDiv.appendChild(title);
                        bookDiv.appendChild(detailsTooltip);
                        detailsTooltip.addEventListener('click', () => {{
                            iframe.src = book.pdf_url;
                            iframeContainer.style.display = 'flex';
                            document.body.style.overflow = 'hidden';  // Disable scrolling
                        }});
                        booksContainer.appendChild(bookDiv);
                    }});
                    closeBtn.addEventListener('click', () => {{
                        iframe.src = '';  // Clear the iframe source
                        iframeContainer.style.display = 'none';
                        document.body.style.overflow = 'auto';  // Enable scrolling
                    }});
                }}
                
                function loadListView(filteredBooks){{
                    const booksContainer = document.getElementById('books');
                    booksContainer.innerHTML = '';  // Clear any previous book data
                    filteredBooks.forEach(book => {{
        const bookDiv = document.createElement('div');
        bookDiv.className = 'book list-view-item';  // Add class for list view

        // Create clickable thumbnail
        const thumbnail = document.createElement('div');
        thumbnail.className = 'thumbnail';
        const img = document.createElement('img');
        if (book.thumbnail_url!=null) {{
            img.src = book.thumbnail_url;
            thumbnail.appendChild(img);
        }}
        // Add event listener to open PDF in iframe on click
        thumbnail.addEventListener('click', () => {{
            iframe.src = book.pdf_url;
            iframeContainer.style.display = 'flex';
            document.body.style.overflow = 'hidden';
        }});

        bookDiv.appendChild(thumbnail);

        // Create book details for list view
        const details = document.createElement('div');
        details.className = 'details';
        details.innerHTML = `
            <h3>${{book.title}}</h3>
            <p><strong>Author:</strong> ${{book.creators.join(', ')}}</p>
            <p><strong>Publisher:</strong> ${{book.publisher}}</p>
            <p><strong>Year:</strong> ${{book.year}}</p>
            <p><strong>Language:</strong> ${{book.language}}</p>
            <p><strong>Subject:</strong> ${{book.subject}}</p>
        `;

        bookDiv.appendChild(details);

        booksContainer.appendChild(bookDiv);
    }});


                    // Close the iframe
                    const closeBtn = document.getElementById('closeBtn');
                    closeBtn.addEventListener('click', () => {{
                        const iframe = document.getElementById('iframe');
                        const iframeContainer = document.getElementById('iframeContainer');
                        iframe.src = '';  
                        iframeContainer.style.display = 'none';
                        document.body.style.overflow = 'auto';  // Enable scrolling
                    }});
                }}
                 document.addEventListener('DOMContentLoaded', () => {{
                 
                    const fullscreenModal = document.getElementById('gandhiImageModal');
                        fullscreenModal.style.display = 'flex';

                        document.addEventListener('click', () => {{
                            fullscreenModal.style.display = 'none';
                        }});
                              
                    const aboutUsModal = document.getElementById('aboutUsModal');
                    const gandhiTrustModal = document.getElementById('gandhiTrustModal');

                    // Get open modal buttons
                    const openAboutUsBtn = document.getElementById('openAboutUs');
                    const openGandhiTrustBtn = document.getElementById('openGandhiTrust');

                    // Get close buttons
                    const closeAboutUsBtn = document.getElementById('closeAboutUs');
                    const closeGandhiTrustBtn = document.getElementById('closeGandhiTrust');

                    // Open the About Us modal
                    openAboutUsBtn.addEventListener('click', () => {{
                        aboutUsModal.style.display = 'block';
                    }});

                    // Open the Gandhi Trust modal
                    openGandhiTrustBtn.addEventListener('click', () => {{
                        gandhiTrustModal.style.display = 'block';
                    }});

                    // Close the About Us modal
                    closeAboutUsBtn.addEventListener('click', () => {{
                        aboutUsModal.style.display = 'none';
                    }});

                    // Close the Gandhi Trust modal
                    closeGandhiTrustBtn.addEventListener('click', () => {{
                        gandhiTrustModal.style.display = 'none';
                    }});

                    // Close modals when clicking outside of them
                    window.addEventListener('click', (event) => {{
                        if (event.target === aboutUsModal) {{
                            aboutUsModal.style.display = 'none';
                        }}
                        if (event.target === gandhiTrustModal) {{
                            gandhiTrustModal.style.display = 'none';
                        }}
                    }});
                    loadBooksInView('grid');
                    initializeFilters();
                    document.getElementById('search-books').addEventListener('input', applyFilters);
                }});
           

            

            
        </script>
    </body>
    </html>
    """

    with open(output_html, "w", encoding='utf-8') as f:
        f.write(html_content)

# Specify the path to your JSON file and the desired output HTML file
json_file = "books.json"
output_html = "index.html"
generate_html_from_json(json_file, output_html)
