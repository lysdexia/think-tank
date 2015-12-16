function (doc) {
	if (doc.doc_type == "User") {
		emit(doc.token, doc);
	}
}
