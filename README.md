**Hello**🖐 **Automated Testing for opencartAwesomeQA Demo Website with Selenium (Pytest, POM, HTML Reports, Jenkins Pipeline)**

This project tests various functionalities of the opencartAwesomeQA demo website, such as valid and invalid login, valid reigster, add to cart, add products in wishlists, and checking out products.
___________________________________________

🎯 **Pre-requisites:**
- Python 3
- Any browsers(Chrome, Firefox, Edge)
___________________________________________

▶ **Test Execution**

Run commands: 
1. Install Dependecies:

       pip install -r requirements.txt
2. Run the test with html report:

       pytest -v --html=report.html 
   or specifying browser

       pytest -v --browser=edge --html=report.html
    

**To run this on jenkins**

1. Add item name, click Pipeline and click OK

   
2. Scroll down find Pipeline and Select pipeline script from SCM

   
3. Choose GIT

   
4. Enter the repo URL and click and save

  
5. Click build now

   



    
   
   
    
