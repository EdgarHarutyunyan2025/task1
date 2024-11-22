async function delayedAddition(a, b) {
  console.log('number1 = 5');
  console.log('number2 = 3');
  await new Promise(resolve => setTimeout(resolve, 2000)); // 2 секунды
  const result = a + b;
  console.log(`sum =  ${result}`);
}

delayedAddition(5, 3);
