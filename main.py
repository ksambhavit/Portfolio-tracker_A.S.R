import portfolio_controller

print(portfolio_controller)
print(dir(portfolio_controller))

def main():
    from portfolio_controller import PortfolioController
    controller = PortfolioController()
    controller.run()

if __name__ == "__main__":
    main()
