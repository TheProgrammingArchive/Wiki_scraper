# Wiki_scraper
 
 Just a simple wikipedia scraper nothing much. 
 
 # Usage:
 Clone the repo first. Now go to https://chromedriver.chromium.org/downloads and select the version of chrome you're running. You can do this by searching chrome://version/.
 Now say you're using chrome 88 then select the one which says download chrome 88. Once in the page download the driver corresponding to your os.
 After downloading the zip, move it to a convenient place and extract it. You'll see a chromedriver.exe or chromedriver (on linux). Now copy the address of where the driver is    located __DONT FORGET TO INCLUDE \chromedriver.exe after the path or \chromedriver (on linux)__

 Now open wiki_mod with an editor. On line 10 you'll see self.PATH in that region paste the path location and you'll be good to go.
 
 # How to scrape:

 wikimod.py -options search_query
 
## Options:
 -b -> view bio/tab
 -c -> page content
 -h -> usage
 
 eg: wikimod.py -c minecraft, will give the page content for minecraft
