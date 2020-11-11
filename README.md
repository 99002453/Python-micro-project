# Python-micro-project

## The Application program is implemented to satisfy the following functionalities:
- [ ] At the beginning the server is ready and is listening to the requests from the clients.
- [ ] when the clients run the connection is established between the server and the client.
- [ ] Once the connection is established,the client starts the Quiz event and prompts the user with the various categories available for the Quiz contest.
- [ ] The client chooses the  category of his interest and the respective CSV file is fetched from the server to the client through socket.
- [ ] In the next step the quiz questions with its options are prompted to the player and is asked to enter his option.
- [ ] After completing all the questions from that category ,a dictionary consisting of the question_id and its respective answer  chosen by the player is sent to the server via the  socket.
- [ ] The server calculates the score of the client by the comparing the user entered answers and the correct answers and sent back to the client,so that the user comes to know his/her knowledge in that category.
- [ ] Finally the user is again taken back to main menu where the user can either continue he game with a different category or exit the quiz by choosing appropriate option. 

![Code Coverage](https://github.com/99002453/Python-micro-project/workflows/Code%20Coverage/badge.svg)
![.github/workflows/build.yml](https://github.com/99002453/Python-micro-project/workflows/.github/workflows/build.yml/badge.svg)

