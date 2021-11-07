var element =  document.querySelector('#chat-text');
element.scrollTop = element.scrollHeight - element.clientHeight;
var user_username = JSON.parse(document.getElementById('user_username').textContent);
if (user_username.length==0){
    user_username = "Anonim"
}
        
function send(e){
    const messageInputDom = document.querySelector('#input');
    const message = messageInputDom.value;

    if(message){
        chatSocket.send(JSON.stringify({
            'message': message,
            'username': user_username,
        }));
        messageInputDom.value = '';
    }
};

const roomName = JSON.parse(document.getElementById('room-name').textContent);
const chatSocket = new WebSocket(
            'ws://' +
            window.location.host +
            '/ws/chat/' +
            roomName +
            '/'
);

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    const time = new Date().toLocaleTimeString(); 
    var user_username = JSON.parse(document.getElementById('user_username').textContent);
    
    var block = document.createElement("div")
    var newP = document.createElement("div")
    newP.innerHTML=data.username;
    var newP2 = document.createElement("div");  
    newP2.innerHTML=data.message;
    block.appendChild(newP)
    block.appendChild(newP2)
            
    if (user_username==data.username){
        block.className = "message personal";
    }else{
        block.className = "message";
    }

    var element =  document.querySelector('#chat-text');
    element.appendChild(block); 
            
    element.scrollTop = element.scrollHeight - element.clientHeight;
}
