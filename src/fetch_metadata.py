import aiohttp
import asyncio

async def fetch_metadata(doc_id):
  """ Asynchronously fetch metadata for a given document ID from a placeholder API and returns none if the request fails """
  try:
    async with aiohttp.ClientSession() as session:
      url = f"https://jsonplaceholder.typicode.com/posts/{doc_id}"
      async with session.get(url, timeout=5) as resp:
          resp.raise_for_status()  # Raise an exception for HTTP errors
          data = await resp.json()
          return data
  except Exception as e:
      print(f"Error fetching metadata for ID {doc_id}: {e}")
      return None
      

async def main():
    """ List of document IDs to fetch metadata concurrently and print results"""
    tasks = [fetch_metadata(i) for i in range(1, 4)]
    # asyyncio.gather will run the requested task concurrently and return the results as list
    results = await asyncio.gather(*tasks)
    for metadata in results:
        print(f"Fetched ID {metadata.get('id')}: {metadata.get('title')}")

async def fetch_safe(session, url):
    """ Asynchronously fetch data from a given URL that returns an error message if the request fails """
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as resp:
            return await resp.text()
    except Exception as e:
        return f"Error fetching {url}: {e}"

if __name__ == "__main__":
    asyncio.run(main())