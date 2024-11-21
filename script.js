async function delayedAddition(a, b) {
  console.log('Задержка начала...');
  await new Promise(resolve => setTimeout(resolve, 2000)); // 2 секунды
  const result = a + b;
  console.log(`Результат сложения: ${result}`);
}

delayedAddition(5, 3);
