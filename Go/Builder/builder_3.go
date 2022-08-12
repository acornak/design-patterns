package main

import (
	"net/mail"
)

type email struct {
	from, to, subject, body string
}

type EmailBuilder struct {
	email email
}

func (b *EmailBuilder) From(from string) *EmailBuilder {
	_, err := mail.ParseAddress(from)
	if err != nil {
		panic("email in incorrect format")
	}
	b.email.from = from
	return b
}

func (b *EmailBuilder) To(to string) *EmailBuilder {
	_, err := mail.ParseAddress(to)
	if err != nil {
		panic("email in incorrect format")
	}
	b.email.to = to
	return b
}

func (b *EmailBuilder) Subject(subject string) *EmailBuilder {
	b.email.subject = subject
	return b
}

func (b *EmailBuilder) Body(body string) *EmailBuilder {
	b.email.body = body
	return b
}

func sendMailImpl(email *email) {

}

type build func(*EmailBuilder)

func SendEmail(action build) {
	builder := EmailBuilder{}
	action(&builder)
	sendMailImpl(&builder.email)
}

// func SendEmail(email email) {}

func main() {
	SendEmail(func(b *EmailBuilder) {
		b.From("foo@bar.com").
			To("bar@baz.com").
			Subject("Meeting").
			Body("Meeting cancelled.")
	})
}
