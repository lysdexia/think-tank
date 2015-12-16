function (doc) {
	if (doc.doc_type == "User") {
		emit(doc.username, {
			"id": doc._id,
			"username": doc.username,
			"password": doc.password,
			"salt": doc.salt,
			"role": doc.role,
			"created": doc.created,
			"modified": doc.modified
		});
	}
}
