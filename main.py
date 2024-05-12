"""
Main module for goodreads api/webscraper project
author: haydenfish
"""

from fastapi import FastAPI, HTTPException, Request
from slowapi.util import get_remote_address
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
import uvicorn
import slowapi

from goodreads import GoodReads

app = FastAPI()
gr = GoodReads()
limiter = slowapi.Limiter(key_func=get_remote_address)

def run():
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

    uvicorn.run("main:app", reload=True)

@app.get("/search/{book_title}")
@limiter.limit("10/minute")
async def search(request: Request, book_title):
    results = gr.scan_result_list(book_title)

    if len(results) < 1:
        raise HTTPException(status_code=404, detail="Could not locate book with title - " + book_title)
    
    return {"results_length": len(results)}, results

@app.get("/details/{book_title}")
@limiter.limit("10/minute")
async def search(request: Request, book_title):
    result = gr.scan_result_item(book_title)

    if result is None:
        raise HTTPException(status_code=404, detail="Could not locate book with title - " + book_title)
    
    return result

@app.get("/quotes/random/{book_title}")
@limiter.limit("10/minute")
async def random_quote(request: Request, book_title):
    quote = gr.find_random_quote(book_title)

    if quote is None:
        raise HTTPException(status_code=404, detail="Could not find any quotes for book title - " + book_title)
    
    return quote

@app.get("/quotes/all/{book_title}")
@limiter.limit("10/minute")
async def quotes(request: Request, book_title):
    quotes = gr.find_all_quotes(book_title)

    if len(quotes) < 1:
        raise HTTPException(status_code=404, detail="Could not find any quotes for book title - " + book_title)
    
    return {"results_length": len(quotes)}, quotes

if __name__ == "__main__":
    run()