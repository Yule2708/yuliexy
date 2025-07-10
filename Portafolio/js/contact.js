const contactForm = document.getElementById('contact-form'),
  contactName = document.getElementById('contact-name'),
  contactEmail = document.getElementById('contact-email'),
  contactSubject = document.getElementById('contact-subject'),
  contactMessage = document.getElementById('contact-message'),
  message = document.getElementById('message');

  const sendEmail =(e) => {
    e.prevenetDefault();

    if(contactName.value == '' || contactEmail.value === "" || contactSudbject.value === '' || 
        contactMessage.value === '' ){
            message.textContent = 'Write all the input fields';
            message.classList.remove('color-first');
            message.classList.add ('color-red');

            setTimeout(() =>{
                message.textContent =''
            }, 3000);
        } else{
            emailjs.
            sendForm(
                'service_640j641', 
                'template_4vf9c4t', 
                '#contact-form', 
                'jByhQgDtLJHN0KgWC'
            )
                .then(
                () => {
                    message.textContent = 'Message sent ';
                    message.classList.add ('color-first');

                    setTimeout(() =>{
                        message.textContent =''
                    }, 5000);
                },
                (error) => {
                  alert('OOPs! SOMETHING WENT WRONG...', error);

                },
              );

              contactName.value ='';
              contactEmail.value ='';
              contactSubject.value ='';
              contactMessage.value ='';
        }
  };

  contactForm.addEventListener ('submil', sendEmail);