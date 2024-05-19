document.addEventListener('DOMContentLoaded', loadBooks);

function loadBooks() {
    const booksContainer = document.getElementById('books');

    fetch('book_identifiers.json')
        .then(response => response.json())
        .then(folders => {
            const first25Folders = folders.slice(0, 25); // Limit to the first 25 folders
            first25Folders.forEach(folder => {
                fetch(`books/${folder}/${folder}_meta.xml`)
                    .then(response => response.text())
                    .then(data => {
                        const parser = new DOMParser();
                        const xml = parser.parseFromString(data, 'application/xml');
                        
                        const title = xml.querySelector('title').textContent;
                        const creators = Array.from(xml.querySelectorAll('creator')).map(creator => creator.textContent);
                        // const description = xml.querySelector('description').textContent;
                        // const date = xml.querySelector('date').textContent;
                        const year = xml.querySelector('year').textContent;
                        const language = xml.querySelector('language').textContent;
                        const subject = xml.querySelector('subject').textContent;
                        const publisher = xml.querySelector('publisher').textContent;
                        const bookDiv = document.createElement('div');
                        bookDiv.className = 'book';
                        bookDiv.dataset.year = year;
                        bookDiv.dataset.author =creators.join(', ');
                        bookDiv.dataset.language = language;
                        bookDiv.dataset.publisher = publisher;
                        bookDiv.dataset.subject = subject;

                        const thumbnail = document.createElement('div');
                        thumbnail.className = 'thumbnail';
                        const img = document.createElement('img');
                        img.src = `books/${folder}/__ia_thumb.jpg`;
                        const readLink = document.createElement('a');
                        readLink.href = `books/${folder}/${folder}.pdf`; // Adjusted URL
                        readLink.appendChild(img);
                        thumbnail.appendChild(readLink);

                        const details = document.createElement('div');
                        details.className = 'details';
                        details.innerHTML = `<h3>${title}</h3><p>Author: ${creators}</p><p>Publisher: ${publisher}</p><p>Year: ${year}</p><p>Language: ${language}</p><p>Subject: ${subject}</p>`;

                        // const link = document.createElement('a');
                        // link.href = `books/${folder}/${folder}.pdf`;
                        // link.textContent = 'Read the book';
                        // details.appendChild(link);

                        bookDiv.appendChild(thumbnail);
                        bookDiv.appendChild(details);

                        booksContainer.appendChild(bookDiv);
                    })
                    .catch(error => console.error('Error fetching XML:', error));
            });
        })
        .catch(error => console.error('Error fetching folder list:', error));
}

function filterBooks() {
    const year = document.getElementById('filter-year').value.toLowerCase();
    const author = document.getElementById('filter-author').value.toLowerCase();
    const language = document.getElementById('filter-language').value.toLowerCase();
    const publisher = document.getElementById('filter-publisher').value.toLowerCase();
    const subject = document.getElementById('filter-subject').value.toLowerCase();

    const books = document.querySelectorAll('.book');
    books.forEach(book => {
        const bookYear = book.dataset.year.toLowerCase();
        const bookAuthor = book.dataset.author.toLowerCase();
        const bookLanguage = book.dataset.language.toLowerCase();
        const bookPublisher = book.dataset.publisher.toLowerCase();
        const bookSubject = book.dataset.subject.toLowerCase();

        if ((year === '' || bookYear.includes(year)) &&
            (author === '' || bookAuthor.includes(author)) &&
            (language === '' || bookLanguage.includes(language)) &&
            (publisher === '' || bookPublisher.includes(publisher)) &&
            (subject === '' || bookSubject.includes(subject))) {
            book.style.display = 'flex';
        } else {
            book.style.display = 'none';
        }
    });
}
