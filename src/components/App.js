import React from 'react';
import {socket} from './Socket';


const App = () => {
    const [receivedData, setReceivedData] = React.useState(undefined);
    
    React.useEffect(() => {
        let isSubscribed = true;
        socket.on("xiaotiancai", receivedData => {
            if(isSubscribed) {
                setReceivedData(receivedData);
            }
        });
        console.log("received");
        console.log(receivedData);
        return () => { isSubscribed = false };
    });

    return (
        <div>
            App
            <div>
                {receivedData}
            </div>
        </div>
    );
}

export default App