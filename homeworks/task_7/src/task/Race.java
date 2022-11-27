package task;

public enum Race {
    Orc(6,12,2),
    Elf(2,9,9),
    Dwarf(6,10,4),
    Halfling(1,8,11),
    Human(6,7,7);
    private int str;
    private int hp;
    private int dex;
    Race(int strength, int health, int dexterity) {
        this.str = strength;
        this.hp = health;
        this.dex = dexterity;
    }
    public int strength() {
        return str;
    }
    public int health() {
        return hp;
    }
    public int dexterity() {
        return dex;
    }
}
