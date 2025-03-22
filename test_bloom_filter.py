from google.cloud import bigquery
from bloom_filter import BloomFilter
import base64

def check_fruit_in_bloom(fruit):
    client = bigquery.Client()
    table_id = "nimble-courier-449405-f7.my_dataset.fruit_bloom_filter"

    query = f"SELECT bit_array FROM `{table_id}` ORDER BY RAND() LIMIT 1"
    query_job = client.query(query)
    results = query_job.result()

    for row in results:
        saved_state = row["bit_array"]

        bloom_filter = BloomFilter(size=len(base64.b64decode(saved_state)))  # Match size!
        bloom_filter.load_state(saved_state)

        if fruit in bloom_filter:
            print(f"✅ '{fruit}' is likely present in the Bloom filter.")
        else:
            print(f"❌ '{fruit}' is NOT present in the Bloom filter.")

# Run the test
if __name__ == "__main__":
    check_fruit_in_bloom("pen")
