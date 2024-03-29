require('dotenv').config()
const fetch = require('node-fetch')
const express = require('express')

const port = process.env.PORT || 3000
const nbTasks = parseInt(process.env.TASKS) || 20

const randInt = (min, max) => Math.floor(Math.random() * (max - min)) + min
const taskType = () => (randInt(0, 2) ? 'mult' : 'add')
const args = () => ({ a: randInt(0, 40), b: randInt(0, 40) })

const generateTasks = (i) =>
  new Array(i).fill(1).map((_) => ({ type: taskType(), args: args() }))

let envWorkersString = process.env.WORKERS.substring(1)
let envWorkers = envWorkersString.split(";")
let workers1 = []
envWorkers.forEach(element => {
  workers1.push(element.split(","))
});
let workers = []
let i = 1
workers1.forEach(element => {
  workers.push({url: `http://worker${i}:${element[0]}`, id:`${i}`, type: `${element[1]}`})
  i++
});


const app = express()
app.use(express.json())
app.use(
  express.urlencoded({
    extended: true,
  })
)

app.get('/', (req, res) => {
  res.send(JSON.stringify(workers))
})

app.post('/register', (req, res) => {
  const { url, id } = req.body
  console.log(`Register: adding ${url} worker: ${id}`)
  workers.push({ url, id })
  res.send('ok')
})

let tasks = generateTasks(nbTasks)
let taskToDo = nbTasks

const wait = (mili) =>
  new Promise((resolve, reject) => setTimeout(resolve, mili))

const sendTask = async (worker, task) => {
  console.log(`=> ${worker.url}/${task.type}`, task)
  workers = workers.filter((w) => w.id !== worker.id)
  tasks = tasks.filter((t) => t !== task)
  const request = fetch(`${worker.url}/${task.type}`, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(task.args),
  })
    .then((res) => {
      workers = [...workers, worker]
      return res.json()
    })
    .then((res) => {
      taskToDo -= 1
      console.log('---')
      console.log(nbTasks - taskToDo, '/', nbTasks, ':')
      console.log(task, 'has res', res)
      console.log('---')
      return res
    })
    .catch((err) => {
      console.error(task, ' failed', err.message)
    })
}

const main = async () => {
  console.log(tasks)
  console.log("string : " + envWorkersString)
  workers.forEach(element => {
    console.log(element)
  });

  while (taskToDo > 0) {
    await wait(100)
    if(workers.length === 0 || tasks.length ===0) continue
    availableWorkers = workers.filter((x) => x.type == tasks[0].type || x.type == "gen") 
    if (availableWorkers.length === 0) continue
    sendTask(availableWorkers[0], tasks[0])
  }
  console.log('end of tasks')
  server.close()
}

const server = app.listen(port, () => {
  console.log(`Register listening at http://planner:${port}`)
  console.log('starting tasks...')
  main()
})
