import sys
from amazon_pricepal.finder import get_amazon_price

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py <amazon_product_url>")
        sys.exit(1)
    url = sys.argv[1]
    try:
        price = get_amazon_price(url)
        print(f"Amazon price: {price}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()