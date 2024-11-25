import requests

def get_mac_vendor(mac_address):
    """Consulta el fabricante de una dirección MAC usando la API de macvendors.com."""
    url = f"https://api.macvendors.com/{mac_address}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text.strip()
        elif response.status_code == 404:
            return "No se encontró el fabricante para esta dirección MAC."
        else:
            return f"Error: {response.status_code}. No se pudo completar la consulta."
    except requests.RequestException as e:
        return f"Error al realizar la consulta: {e}"

def main():
    print("Consulta de fabricante por dirección MAC")
    mac_address = input("Ingresa la dirección MAC (formato 00:1A:2B:3C:4D:5E): ").strip()
    vendor = get_mac_vendor(mac_address)
    print(f"Fabricante: {vendor}")

if __name__ == "__main__":
    main()
