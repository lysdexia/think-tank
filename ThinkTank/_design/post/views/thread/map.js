function (doc) {
	if (doc.doc_type == "Post") {
		emit(doc.thread, doc);
	}
}
