echo ">> FETCHING UPSTREAM..."
 https://github.com/TSFDX/dzzz /dzzz
echo ">> INSTALLING REQUIREMENTS..."
cd /dzzz
pip3 install -U -r requirements.txt
echo ">> STARTING MUSIC PLAYER USERBOT..."
clear
echo "
#     #                        
##   ## #    #  ####  #  ####  
# # # # #    # #      # #    # 
#  #  # #    #  ####  # #      
#     # #    #      # # #      
#     # #    # #    # # #    # 
#     #  ####   ####  #  ####  
                               
######                                    
#     # #        ##   #   # ###### #####  
#     # #       #  #   # #  #      #    # 
######  #      #    #   #   #####  #    # 
#       #      ######   #   #      #####  
#       #      #    #   #   #      #   #  
#       ###### #    #   #   ###### #    # 
                                          
MUSIC PLAYER USERBOT IS SUCCESSFULLY DEPLOYED!
"
python3 main.py
