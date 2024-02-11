import {change_stock_price,change_percentage} from "./elementupdater.mjs";
export async function FIREBASE_GetName(){
  const name = "stock_price"
  const DateRef = firebase.database().ref(`${name}`);
  let stock_price = 0; 

  await DateRef.once('value', (snapshot) => {
    let stockdata = snapshot.val();
    stock_price = stockdata 
  });

  return stock_price;
}

export function FIREBASE_StartListening(){
  
  const stock_price_Ref = firebase.database().ref(`stock_price`);
  const percentage_Ref = firebase.database().ref(`pge`);

  stock_price_Ref.on('value', (snapshot) => {
    let stock_price = snapshot.val();
    change_stock_price(stock_price)
  });


  percentage_Ref.on('value', (snapshot) => {
    let percentage = snapshot.val();
    change_percentage(percentage)
  });
}


