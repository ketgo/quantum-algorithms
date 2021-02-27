# Quantum Algorithms

The repository contains collection of jupyter notebooks on quantum computer algorithms. The notebooks contains basic to andvanced concepts, research ideas, and implementation of Quantum Circuits and Algorithms. The `qiskit` package is used in all the notebooks for building and simulating Quantum Circuits.

## Deployment

All the notebooks can be accessed by deploying a jupyter-notebook server and installing `qiskit` python package. The recomended way to deploy the server is to use the provided `docker-compse.yaml` file.
```bash
  $ docker-compose up -d
```
When the deployment is done, the URL for the jupyter server can be obtained from the logs. To do so just run: 
```bash
  $ docker-compose logs
```

To bring down the server run the following command:
```bash
  $ docker-compose down
```

## License

MIT License

## Resources

- (Qiskit Texbook)[https://qiskit.org/textbook/preface.html]

