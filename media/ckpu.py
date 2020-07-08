
{% load static %}



{% static "img" as baseURL %}

{% static "img/font_previews" as font_previews %}

<!DOCTYPE html>

<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">

  <title>Handwriting Synthesis</title>
  <meta content="" name="descriptison">
  <meta content="" name="keywords">

  <!-- Favicons -->
  <link href="{% static 'img/favicon.png'%}" rel="icon">
  <link href="{% static 'img/apple-touch-icon.png'%}" rel="apple-touch-icon">

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Montserrat:300,300i,400,400i,500,500i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="{% static '/vendor/bootstrap/css/bootstrap.min.css'%}" rel="stylesheet">
  <link href="{% static '/vendor/icofont/icofont.min.css'%}" rel="stylesheet">
  <link href="{% static '/vendor/boxicons/css/boxicons.min.css'%}" rel="stylesheet">
  <link href="{% static '/vendor/venobox/venobox.css'%}" rel="stylesheet">
  <link href="{% static '/vendor/owl.carousel/assets/owl.carousel.min.css'%}" rel="stylesheet">
  <link href="{% static '/vendor/aos/aos.css'%}" rel="stylesheet">

  <!-- Template Main CSS File -->
  <link href="{% static '/css/style.css'%}" rel="stylesheet">


  <script
  src="https://code.jquery.com/jquery-3.4.1.js"
  integrity="sha256-WpOohJOqMqqyKL9FccASB9O0KwACQJpFTUBLTYOVvVU="
  crossorigin="anonymous"></script>

<style>
.responsive {
  width: 100%;
  height: auto;
}
</style>


</head>

<body>

 {% if user.is_authenticated %}
  <!-- ======= Home Section ======= -->
  
  <!-- ======= Header ======= -->
  <header id="header" class="d-flex align-items-center">
    <div class="container">

      <!-- The main logo is shown in mobile version only. The centered nav-logo in nav menu is displayed in desktop view  -->
      <div class="logo d-block d-lg-none">
        <a href="index.html"><img src="{% static '/img/logo.png'%}" alt="" class="img-fluid"></a>
      </div>

      <nav class="nav-menu d-none d-lg-block">
        <ul class="nav-inner">
          <li class="active"><a href="index.html">Home</a></li>
          <li class="drop-down"><a href="">About</a>
            <ul>
              <li><a href="#about">About Us</a></li>
              <li><a href="#team">Team</a></li>

              <li class="drop-down"><a href="#">Deep Drop</a>
                <ul>
                  <li><a href="#">Deep Drop Down 1</a></li>
                  <li><a href="#">Deep Drop Down 2</a></li>
                  <li><a href="#">Deep Drop Down 3</a></li>
                  <li><a href="#">Deep Drop Down 4</a></li>
                  <li><a href="#">Deep Drop Down 5</a></li>
                </ul>
              </li>
            </ul>
          </li>
          <li><a href="#services">Services</a></li>

          <li class="nav-logo"><a href="index.html"><img src="{% static '/img/logo.png'%}" alt="" class="img-fluid"></a></li>

          <li><a href="#portfolio">Portfolio</a></li>
          <li><a href="#pricing">Pricing</a></li>
          

        </ul>
      </nav><!-- .nav-menu -->

    </div>
  </header><!-- End Header -->

  <main id="main">




    <!-- ======= About Us Section ======= -->
    <section id="download" class="about">
      <div class="container">
        <div class="section-title" data-aos="fade-up">
         <h2>Create your own fonts in 2 easy steps!</h2>
          <h6>You are logged in as <strong>{{user.username}}</strong></h6>
          <br>
          <h2>Step 1/2</h2>
          <h5>Download, fill and scan the template.</h5>
          <p>Note- Scanning using a Physical Document Scnner like one attached to a printer is highy recommended. Results might <strong>totally</strong> fail otherwise</p>
        </div>

        <div class="row">
          <div class="col-lg-12" data-aos="fade-right">
            <div class="image">
             <h5><a href="https://drive.google.com/file/d/1znycJm6SZ4gkc4HKGJgw_uGhxraE8HHf/view?usp=sharing">Click Here To Download</a></h5>
             <p>Google Drive Link</p>
            </div>
          </div>          
        </div>

      </div>
    </section><!-- End About Us Section -->



    <!-- ======= Services Section ======= -->
    <section id="upload" class="services">
      <div class="container">

        <div class="section-title" data-aos="fade-up">
          <h2>Step 2/2</h2>
          <h5>Upload the scanned files</h5>
          <p>Note- Files must be Image Files.</p>
          <p>Warning- Scanning using a Physical Document Scnner like one attached to a printer is highy recommended. Results might <strong>totally</strong> fail otherwise</p>
        </div>

        <div class="row" id = 'step2'>
          <div class="col-lg-6 order-2 order-lg-1">
            <div class="icon-box mt-5 mt-lg-0" data-aos="fade-up">
              <i class="bx bx-receipt"></i>
              <form  id='templateupload' name='templateupload' method="post" enctype="multipart/form-data" >
                {% csrf_token %}
              <h4>Upload File 1/3</h4>
              <input type="file" id="template1" name="template1" accept="image/*" required>
            </div>
            <div class="icon-box mt-5" data-aos="fade-up" data-aos-delay="100">
              <i class="bx bx-cube-alt"></i>
              <h4>Upload File 2/3</h4>
              <input type="file" id="template2" name="template2" accept="image/*" required>
            </div>
            <div class="icon-box mt-5" data-aos="fade-up" data-aos-delay="200">
              <i class="bx bx-images"></i>
              <h4>Upload File 3/3</h4>
              <input type="file" id="template3" name="template3" accept="image/*" required>
            </div>
            <div class="icon-box mt-5" data-aos="fade-up" data-aos-delay="300">
              <i class="bx bx-shield"></i>
              <h4>Submit</h4>
              <button type="submit">Submit</button>
              
  
              </form> 
              
              
              <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
             <script type="text/javascript">
              // form upload
              $('#templateupload').submit(function(e){
                  e.preventDefault();
                  $form = $(this)

                  var formData = new FormData(this);
                  $.ajax({
                     url: "{% url 'main:templateupload' %}",
                      type: 'POST',
                      data: formData,
                      cache: false,
                      contentType: false,
                      processData: false,
                      success: function (json) {
                          fontID=json.id
                          
                          $("#succes").replaceWith( '<br>'+'<h4  id = "succes">' +' Font Created Sucesfully, Font Id- #'+ json.id + '</h4> <h6>This width setting reffers to number of charaters that can be rendered <strong>per line</strong> it depends on width of charatersas per user.</h6> <h6> Adjust the width setting so that all words are completely inside the page dimentions </h6>' )
                          $("#step2").replaceWith( '<br>'+'<div class="section-title" data-aos="fade-up">'+'<h4 id = "succes">' +' Font Created Sucesfully, Font Id- #'+ json.id + '</h4>'+'</div>' )
                          $("#image_placeholder").replaceWith( "<img id='image_placeholder' class='responsive' src='/media/font_preview/"+json.font_preview+ "' alt='Font Preview'> ")
                          $("#widthsetting").replaceWith(" <label for='width'> Width (between 40 and 60):</label> <input type='number' id='width' name='width' min='40' max='60' value='55'>" + "<input type='submit'>")
                          

                      },
                      
                    });
                });
                // end
               </script>

            </div>
          </div>
          <div class="image col-lg-4 order-1 order-lg-2" style='background-image: url("{{baseURL}}/form.png");' data-aos="fade-left" data-aos-delay="100"></div>

        </div>

      </div>
    </section><!-- End Services Section -->



 <!-- ======= Pricing Section ======= -->
    <section id="text" class="why-us">
      <div class="container-fluid">

        <div class="section-title" data-aos="fade-up">
          <h2 id='demo'>Result</h2>
          <h5 id='succes'> waiting for submission...</h5>
         


          <form id='ok' name='ok' method="post"> 
            {% csrf_token %} 
            <h1 id='widthsetting'> </h1>
           </form>

      <script>
        width='55'
      </script>      

    <script src="{% static 'js/jquery-2.2.4.min.js'%}"></script>
    <script src="{% static 'js/bootstrap.min.js'%}"></script> 
            <script>
              
            $('#ok').submit(function(e){
                  e.preventDefault();

                  width= $('#width').val()
                  document.getElementById("demo").innerHTML = width;
                  var unique = $.now();
                  
                  $.ajax({
                      url: "{% url 'main:preview_tinkering' %}",
                      type: 'POST',
                      data: {width: $('#width').val(),
                            fontID: fontID,
                            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                             action: 'post'},
                   
                      success: function (json) {
                          
  $("#image_placeholder").replaceWith( "<img id='image_placeholder' class='responsive' src='/media/font_preview/"+json.font_preview+'?'+unique+"'>")
                        
                      },
                      
                    });
                });
                // end
               </script>




        <div class="row">

          <div class="col-lg-7 order-2 order-lg-1 d-flex flex-column justify-content-center align-items-stretch">

            <div class="content" data-aos="fade-up">
              <h5 id='widthsetting'>Have a good look to see how this works-</strong></h5>
              
              <pre><p style="text-align:left;"><strong>Text File that is used to create this preview-</strong>
If it looks too random, Try tweaking the setting when in 'Render Text' section

Que. 1
How do I create a question tag like this?
Ans.
Tags 'Que.' and 'Ans.' are keywords that are automatically shifted on the left side of margin.
Important- Don't forget to move to the next line(Press Enter) after using these tags.

Que. 2
How do I create a numbered list?
Ans.
1. If the first thing to appear in a line is a number it is automatically shifted to the left of the margin
2.0 If you don't want the first character to shifted-
2.a) Add a '|' before the number, Example-
1500 lines of code are behind this software (Website excluded)
|1500 lines of code are behind this software (Website excluded)

Que. 2
What are the mathematic features available?
Ans.
Text between two '^' is shifted as power- A
Example- 10 ^2^ + 100 ^(-12/13)^ E=mc ^2^

You can explore the 'Example' section for more examples about what all can be done!
                  </p></pre>


               <h6> Note- 
                 <strong> Medium Randomness</strong> is used to create this render.
                  </h6>
                  <p>
                  If it looks a little shady, Try tweaking the setting when in <strong>'Render Text'</strong> section
                  </p>
                  <p>
                  There are a lot of settings you can play with to get your ideal output. 
                  </p>
                  <p>
                  Otherwise use can alwas use one from predefined settings, they'll work for shure.
                   </p>
                                             

 


            </div>

            

          </div>

            <div class="col-sm-5 order-1 order-sm-2 align-items-stretch video-box" data-aos="zoom-in">
            <p id='image_placeholder'>Waiting for submission...</p>
            
            <!img id='image_placeholder' class='responsive' src= '/media/fonts/100/1000.png' alt='Font Preview'>
            <br><br><br>


            <div class="col-lg-12 order-2 " data-aos="zoom-in"> 
            <h6>Make shure you read instructions</h6> <h6>and adjust width settings before you submit</h6>
            <p>You <strong>CAN</strong> adjust it afterwards always</p>
            <br>
            
           
            

            <form action='' id='formconfirm' name='formconfirm' method="post" > 
            {% csrf_token %} 
            <input type="text" id="width" name="width" style="display: none;" >
            <input type="text" id="fontID" name="fontID" style="display: none;">
            <button type="submit">Submit</button>
            </form>
              
            
             <script>
              
            $('#formconfirm').submit(function(e){
                  
                  $.ajax({
                      url: "{% url 'main:save_preview' %}",
                      type: 'POST',
                      data: {width: width,
                            fontID: fontID,
                            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                             action: 'post'},
                   
                      success: function (json) {
                          $("#placeholder").replaceWith( "<h1> Hello </h1>") 
                      },
                      
                    });
                });
                // end
               </script>




            </div>
  
            
            </div>
           

       
        </div>

      </div>
    </section><!-- End Why Us Section -->
          
          
          
          
          
          
          



    <!-- ======= Clients Section ======= -->
    <section id="clients" class="clients">
      <div class="container">

        <div class="row">

          <div class="col-lg-2 col-md-4 col-6" data-aos="zoom-in">
            <img src="{% static '/img/clients/python.png'%}" class="img-fluid" alt="">
          </div>

          <div class="col-lg-2 col-md-4 col-6" data-aos="zoom-in" data-aos-delay="100">
            <img src="{% static '/img/clients/opencv.png'%}" class="img-fluid" alt="">
          </div>

          <div class="col-lg-2 col-md-4 col-6" data-aos="zoom-in" data-aos-delay="200">
            <img src="{% static '/img/clients/pillow.png'%}" class="img-fluid" alt="">
          </div>

          <div class="col-lg-2 col-md-4 col-6" data-aos="zoom-in" data-aos-delay="300">
            <img src="{% static 'img/clients/numpy.png'%}" class="img-fluid" alt="">
          </div>

          <div class="col-lg-2 col-md-4 col-6" data-aos="zoom-in" data-aos-delay="400">
            <img src="{% static '/img/clients/django.png'%}" class="img-fluid" alt="">
          </div>

          <div class="col-lg-2 col-md-4 col-6" data-aos="zoom-in" data-aos-delay="500">
            <img src="{% static '/img/clients/auto.png'%}" class="img-fluid" alt="">
          </div>

        </div>

      </div>
    </section><!-- End Clients Section -->


</main>


  <!-- ======= Footer ======= -->
  <footer id="footer">

    <div class="footer-top">

      <div class="container">

        <div class="row justify-content-center">
          <div class="col-lg-6">
            <a href="#header" class="scrollto footer-logo"><img src="{% static '/img/hero-logo.png'%}" alt=""></a>
            <h3>Handwriting Simulator</h3>
            <p>CONVERT PLAIN TEXT INTO YOUR VERY OWN HANDWITING</p>
          </div>
        </div>

        <div class="row footer-newsletter justify-content-center">
          <div class="col-lg-6">
            <form action="" method="post">
               {% csrf_token %} 
              <input type="email" name="email" placeholder="Enter your Email"><input type="submit" value="Subscribe">
            </form>
          </div>
        </div>

        <div class="social-links">
          <a href="#" class="twitter"><i class="bx bxl-twitter"></i></a>
          <a href="#" class="facebook"><i class="bx bxl-facebook"></i></a>
          <a href="#" class="instagram"><i class="bx bxl-instagram"></i></a>
          <a href="#" class="google-plus"><i class="bx bxl-skype"></i></a>
          <a href="#" class="linkedin"><i class="bx bxl-linkedin"></i></a>
        </div>

      </div>
    </div>

    <div class="container footer-bottom clearfix">
      <div class="copyright">
        &copy; Copyright <strong><span>Sanidhya Agrawal</span></strong>. All Rights Reserved
      </div>
    </div>
  </footer><!-- End Footer -->

{% else %}

  <!-- ======= Footer ======= -->
  <footer id="footer">

    <div class="footer-top">

      <div class="container">

        <div class="row justify-content-center">
          <div class="col-lg-6">
            <a href="#header" class="scrollto footer-logo"><img src="{% static '/img/hero-logo.png'%}" alt=""></a>
            <h3>Hey Hacker</h3>
            <p>You need to login first to create your own font</p>
            <br>
             <form action="/#onboarding" method="post" role="form"  data-aos="fade-left">
              {% csrf_token %}
            <button type="submit">Click here to go to login/signup page</button></div>
           </form>>
          </div>
        </div>

        <div class="social-links">
          <a href="#" class="twitter"><i class="bx bxl-twitter"></i></a>
          <a href="#" class="facebook"><i class="bx bxl-facebook"></i></a>
          <a href="#" class="instagram"><i class="bx bxl-instagram"></i></a>
          <a href="#" class="google-plus"><i class="bx bxl-skype"></i></a>
          <a href="#" class="linkedin"><i class="bx bxl-linkedin"></i></a>
        </div>

      </div>
    </div>

    <div class="container footer-bottom clearfix">
      <div class="copyright">
        &copy; Copyright <strong><span>Sanidhya Agrawal</span></strong>. All Rights Reserved
      </div>
    </div>
  </footer><!-- End Footer -->

{% endif %}

  <a href="#" class="back-to-top"><i class="icofont-simple-up"></i></a>

  <!-- Vendor JS Files -->
  <script src="{% static '/vendor/jquery/jquery.min.js'%}"></script>
  <script src="{% static '/vendor/bootstrap/js/bootstrap.bundle.min.js'%}"></script>
  <script src="{% static '/vendor/jquery.easing/jquery.easing.min.js'%}"></script>
  <script src="{% static '/vendor/php-email-form/validate.js'%}"></script>
  <script src="{% static '/vendor/jquery-sticky/jquery.sticky.js'%}"></script>
  <script src="{% static '/vendor/venobox/venobox.min.js'%}"></script>
  <script src="{% static '/vendor/isotope-layout/isotope.pkgd.min.js'%}"></script>
  <script src="{% static '/vendor/owl.carousel/owl.carousel.min.js'%}"></script>
  <script src="{% static '/vendor/aos/aos.js'%}"></script>

  <!-- Template Main JS File -->
  <script src="{% static '/js/main.js'%}"></script>





</body>
</html>

