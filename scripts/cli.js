const spawn = require('child_process').spawn;

let args = process.argv.filter((v, i) => i >= 2);
const pemPath = args.pop();
const intanceTag = args.pop();

function deploy(ip) {
  console.log(`Deploying to: ${ip}`)
  let child = spawn('./scripts/ssh.sh', [pemPath, ip]);
  process.stdin.pipe(child.stdin);

  child.stdout.on('data', (data) => {
    console.log(`${data}`);
  });
}

function flattenDeep(array) {
  return array.reduce((acc, val) => {
    return Array.isArray(val) ? acc.concat(flattenDeep(val)) : acc.concat(val);
  }, []);
}

function fetchIpAddresses(args) {
  const jsonObj = JSON.parse(JSON.parse(JSON.stringify(args.join(''))));
  let instancesArray = jsonObj.map((array) => flattenDeep(array[0]));
  let allByTagNameAndRunning = instancesArray.filter(item => {
    if (item.indexOf(intanceTag) >= 0 && item.indexOf('running') >= 0) {
      return item;
    }
  })
  let ipAddresses = allByTagNameAndRunning.map(i => i[1])
  ipAddresses.forEach(ip => deploy(ip))
}

fetchIpAddresses(args);