require('dotenv').config();
const fs = require('fs');
const Binance = require('node-binance-api');
const MARKET = 'BTCBUSD';

const binance = new Binance().options({
    APIKEY: process.env.API_KEY,
    APISECRET: process.env.API_SECRET
});

const sleep = (timeMs) => new Promise(resolve => setTimeout(resolve, timeMs));

const fechaActual = new Date();
const segundosDesde1970 = Math.floor(fechaActual.getTime());
const medicionTime = 1690247520;
const velas = {};
let time_viejo = 0;
const nombreArchivo = 'precios21.csv'

console.clear();

//Funcion que agrega contenido csv al archivo. Si el archivo no existe lo crea
function grabar(contenido, nombreArchivo){

  fs.readFile(nombreArchivo, 'utf8', (err, data) => {
    if (err) {
      // Si el archivo no existe o hay algún error al leerlo, se crea uno nuevo con la nueva información.
      fs.writeFile(nombreArchivo, contenido, (err) => {
        if (err) {
          console.error('Error al crear el archivo:', err);
        } else {
          console.log('Archivo creado exitosamente con la nueva información.');
        }
      });
    }// else {
      // Si el archivo existe, se agrega la nueva información al contenido existente.
    const nueva_info = data + '\n' +contenido;

    fs.writeFile(nombreArchivo, nueva_info, (error) => {//Agrego datos al archivo
      if (error) {
        console.error('Error al grabar el archivo:', error);
      } else {
        console.log('El archivo CSV ha sido grabado exitosamente:', nombreArchivo);
      }
      });
    //}
  });
}


function leer_velas(tiempo_fin){//Leo un conjunto de velas
  binance.candlesticks("BTCUSDT", "1m", (error, ticks, symbol) => {
    //console.info("Velas registradas:", ticks);
  const contenido_CSV = ticks.map(row => row.join(',')).join('\n');

  fs.readFile(nombreArchivo, 'utf8', (err, data) => {
    if (err) {
      // Si el archivo no existe o hay algún error al leerlo, se crea uno nuevo con la nueva información.
      fs.writeFile(nombreArchivo, contenido, (err) => {
        if (err) {
          console.error('Error al crear el archivo:', err);
        } else {
          console.log('Archivo creado exitosamente con la nueva información.');
        }
      });
    }
  })


    grabar(contenido_CSV, nombreArchivo)
/**************************************************************************************** */
    let first_tick = ticks[0];
    let [time, open, high, low, close, volume, closeTime, assetVolume, trades, buyBaseVolume, buyAssetVolume, ignored] = first_tick;
    time_viejo = time;
  }, {limit: 10, endTime: tiempo_fin});
}


async function imprimir_varios(){
  const bloque = 60000000;
  const limite = 1;
  const tiempo_1ago = 1690929180000;

  for (i=1; i<=limite; i++){
    const tiempo = tiempo_1ago - ((limite - i) * bloque);
    leer_velas(tiempo);
    await sleep(2000);
  }
}

imprimir_varios();


/*
binance.candlesticks("BTCUSDT", "1m", (error, ticks, symbol) => {
    //console.info("Velas registradas:", ticks);
    contenido_CSV = ticks.map(row => row.join(',')).join('\n');
    grabar(contenido_CSV, nombreArchivo)
/**************************************************************************************** */
  /*  let first_tick = ticks[0];
    let [time, open, high, low, close, volume, closeTime, assetVolume, trades, buyBaseVolume, buyAssetVolume, ignored] = first_tick;
    time_viejo = time;
  }, {limit: 5, endTime: segundosDesde1970});
/***************************************************************************************** */

    /**console.log("Time: " + time);
    console.log("Tiempo en segundos: "+ time/1000);
    console.log("Open: "+ open);
    console.log("High: "+ high);
    console.log("Low: "+ low);
    console.log("Close: "+ close);
    console.log("Volume: "+ volume);
    console.log("Close Time: "+ closeTime);
    console.log("assetVolume: "+ assetVolume);
    console.log("trades: "+ trades);**/
    //console.info(symbol+" last close: "+close);
    
    /*
    velas[0]=[//Le pongo el titulo al csv para que tengan nombres las columnas
        'Time',
        'open',
        'high',
        'low',
        'close',
        'volume',
        'closeTime',
        'assetVolume',
        'trades',
        'buyBaseVolume',
        'buyAssetVolume',
        'ingnored'
      ]*/
    //console.log(ticks[0]);
/*************************************************************************** */
/********    Grabo todo en contenido2CSV ***************************** */
    //const contenido2CSV = velas.map(row => row.join(',')).join('\n');
    //const nombreArchivo2 = 'precios.csv';
    //console.log("APA" + segundosDesde1970);
/********************************************************************* */
/** 
    const datos = [
      ['Nombre', 'Edad', 'Correo electrónico'],
      ['Juan', 25, 'juan@example.com'],
      ['María', 30, 'maria@example.com'],
      ['Pedro', 35, 'pedro@example.com']
    ];
    
    const contenidoCSV = datos.map(row => row.join(',')).join('\n');
    const nombreArchivo = 'datos.csv';
    
    fs.writeFile(nombreArchivo, contenidoCSV, (error) => {
      if (error) {
        console.error('Error al grabar el archivo:', error);
      } else {
        console.log('El archivo CSV ha sido grabado exitosamente:', nombreArchivo);
      }
    });
*/
/** 

try{
    await binance.prices(MARKET, (error, ticker) => {
    precio_actual = ticker.BTCBUSD;
    if(error) console.log("Error de lectura de datos");
    });
}catch(error) {console.log(error)};//continue;}
console.log(precio_actual);
*/
/*
Get Kline/candlestick data for a symbol
You can use the optional API parameters for getting historical candlesticks, these are useful if you want to import data from earlier back in time. Optional parameters: limit (max/default 500), startTime, endTime.
// Intervals: 1m,3m,5m,15m,30m,1h,2h,4h,6h,8h,12h,1d,3d,1w,1M
binance.candlesticks("BNBBTC", "5m", (error, ticks, symbol) => {
console.info("candlesticks()", ticks);
let last_tick = ticks[ticks.length - 1];
let [time, open, high, low, close, volume, closeTime, assetVolume, trades, buyBaseVolume, buyAssetVolume, ignored] = last_tick;
console.log(time);
console.log(volume);
console.info(symbol+" last close: "+close);
}, {limit: 500, endTime: 1514764800000});
*/