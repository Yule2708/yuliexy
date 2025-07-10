const contactForm = document.getElementById('contact-form'),
  contactName = document.getElementById('contact-name'),
  contactEmail = document.getElementById('contact-email'),
  contactSudbject = document.getElementById('contact-subject'),
  contactMessage = document.getElementById('contact-message'),
  message = document.getElementById('message');

  const sendEmail =(e) => {
    e.prevenetDefault();

    if(contactName.value == '' || contactEmail.value === "" || contactSudbject.value === '' || 
        contactMessage.value === '' ){
            message.textContent = 'Write all the input fields';
            message.classList.add ('color-red')

            setTimeout(() =>{
                message.textContent =''
            }, 3000);
        }
  };

  contactForm.addEventListener ('submil', sendEmail);