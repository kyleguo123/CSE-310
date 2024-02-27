import {change_stock_price,change_percentage,change_chart} from "./elementupdater.mjs";
export async function FIREBASE_GetPrice(){
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
  const percentage_Ref = firebase.database().ref(`percentage`);
  const stock_date_Ref = firebase.database().ref(`stock_data`);

  stock_price_Ref.on('value', (snapshot) => {
    let stock_price = snapshot.val();
    change_stock_price(stock_price)
  });


  percentage_Ref.on('value', (snapshot) => {
    let Percentage = snapshot.val();
    change_percentage(Percentage)
  });

  stock_date_Ref.on('value', (snapshot) => {
    let stock_data = snapshot.val();
    console.log(stock_data)
    change_chart(stock_data)
  });
}
