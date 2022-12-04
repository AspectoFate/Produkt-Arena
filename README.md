# Produkt-Arena
Explaning all the bugs in each program.

auto_email_sender:  "from May 30, 2022, ​​Google no longer supports the use of third-party apps or devices which ask you to sign in to your Google Account using only your username and password." 
url= "https://support.google.com/accounts/answer/6010255?hl=en#zippy=%2Cif-less-secure-app-access-is-on-for-your-account%2Cif-less-secure-app-access-is-off-for-your-account"

extracting Table from PDF: 
    ModuleNotFoundError: No module named 'ghostscript'. Even after installing "ghostscript" the program sends out the same error.

resume_parsing: 
    there is an error with "return open(output_filepath).read()" command. Made the program run with adding "return open(output_filepath, errors="ignore").read()". The program doesn't parse the data good but it works.

red_talk_video_download:  

    File "c:\Users\anes0\Desktop\Produkt Arena\ted_talk_video_download.py", line 27, in <module>
        result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'group

tried to fix with try-except block.

try:
    result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")
except AttributeError:
    result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result)

new error: 
    File "c:\Users\anes0\Desktop\Produkt Arena\ted_talk_video_download.py", line 33, in <module>
        mp4_url = result_mp4.split('"')[0]
                 ^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'split'

"AttributeError: 'NoneType' object has no attribute 'split'" occurs when we try to call the split() method on a None value, e.g. assignment from function that doesn't return anything. 