FROM golang:1.22-alpine AS builder

WORKDIR /usr/golang 

COPY . .
RUN CGO_ENABLED=0 go build -o /usr/golang/build/fizzbuzz

FROM gcr.io/distroless/static-debian12
COPY --from=builder /usr/golang/build/fizzbuzz /fizzbuzz
COPY --from=builder /usr/golang/templates/index.html /templates/index.html

CMD ["./fizzbuzz", "serve"]