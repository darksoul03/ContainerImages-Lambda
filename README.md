# Container Images with Lambda

This repo is to implement container images with Lambda, specifically for Python Packages greater than 250MB.

## Installation

- Create Docker Image Repository at ECR
- Push the docker image in ECR.

```bash
- docker build -t docker-lambda .
- docker push image-url/docker-lambda
```
Add tags if required.
- Create Lambda with container using the recently pushed image. 
- Test your lambda
 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
