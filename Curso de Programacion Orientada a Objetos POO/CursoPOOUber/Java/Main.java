class Main {
 
    public static void main(String[] args) {
        System.out.println("Hola mundo");
        UberX uberX = new UberX("AMQ123", new Account("Andres Herrera", "AND123"),"Chevrolet","Sonia");
        uberX.setPassenger(4);
        uberX.printDataCar();

        UberVan uberVan = new UberVan("FGH123", new Account("Andres Herrera", "AND123"));
        uberVan.setPassenger(6);


    }   

}