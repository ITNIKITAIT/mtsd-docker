FROM golang:1.22-alpine

WORKDIR /usr/golang 

COPY go.mod go.sum ./

RUN go mod download

COPY . .

RUN go build -o fizzbuzz

CMD ["./fizzbuzz", "serve"]