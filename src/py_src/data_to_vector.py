from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

def data_loading(filetype, folder = "../data/pdf"):
    if(filetype == "pdf"):
        loader = PyPDFLoader(folder)
        
    docs = loader.load()
    print(f"This Docs has {len(docs)} pages")
    
    return docs

def Chuck_Spliting(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    print(f"split document into {len(splits)} part")
    print(splits)
    return splits

def Embedding_Model(
    model_name = "all-MiniLM-L6-v2",
    model_kwargs = {"device": 'cpu'},
    encode_kwargs = {'normalize_embeddings': False}
):
    embeddings = HuggingFaceEmbeddings(
        model_name = model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    return embeddings


def main():
    dir = '../data'
    embedding = Embedding_Model()
    print(f"Recursively listing all items in: {os.path.abspath(dir)}\n")

    for dirpath, dirnames, filenames in os.walk(dir):
        if(len(dirnames) != 0): continue
        docname = dirpath.split('/')[-1]
        # print(f"docname : ", docname)
        des_doc = "../vectorDB" + dirpath[7:]

        for name in filenames:
            des_der = f"{des_doc}/{name}"
            
            if not os.path.exists(des_der):
                os.makedirs(des_der)
            
            folder = os.path.join(dirpath,name)
            split = name.split(".")
            filetype = split[1]
            filename = split[0]
            docs = data_loading(folder = folder, filetype=filetype)
            splits = Chuck_Spliting(docs)
            texts_from_splits = [doc.page_content for doc in splits]
            metadatas_from_splits = [doc.metadata for doc in splits]
            
            # vector transform
            print(des_der)
            vector_store = Chroma.from_texts(
                texts=texts_from_splits,
                embedding=embedding,
                metadatas=metadatas_from_splits,
                persist_directory=des_der
            )
        print("-" * 20)

if __name__ == "__main__":
    main()