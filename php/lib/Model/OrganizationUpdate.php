<?php
/**
 * OrganizationUpdate
 *
 * PHP version 7.4
 *
 * @category Class
 * @package  Tripartie\Tpdk
 * @author   OpenAPI Generator team
 * @link     https://openapi-generator.tech
 */

/**
 * Tripartie
 *
 * Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.
 *
 * The version of the OpenAPI document: 2.0.0.b1
 * Contact: noc@tripartie.com
 * Generated by: https://openapi-generator.tech
 * OpenAPI Generator version: 6.5.0
 */

/**
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

namespace Tripartie\Tpdk\Model;

use \ArrayAccess;
use \Tripartie\Tpdk\ObjectSerializer;

/**
 * OrganizationUpdate Class Doc Comment
 *
 * @category Class
 * @description 
 * @package  Tripartie\Tpdk
 * @author   OpenAPI Generator team
 * @link     https://openapi-generator.tech
 * @implements \ArrayAccess<string, mixed>
 */
class OrganizationUpdate implements ModelInterface, ArrayAccess, \JsonSerializable
{
    public const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $openAPIModelName = 'Organization-Update';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $openAPITypes = [
        'name' => 'string',
        'vatNumber' => 'string',
        'commercialRegistryNumber' => 'string',
        'websiteUrl' => 'string',
        'customBaseUrl' => 'string',
        'billingAddress' => '\Tripartie\Tpdk\Model\OrganizationUpdateBillingAddress',
        'primaryColor' => 'string',
        'secondaryColor' => 'string',
        'accentColor' => 'string',
        'errorColor' => 'string',
        'infoColor' => 'string',
        'successColor' => 'string',
        'warningColor' => 'string',
        'endUserNotificationToggle' => 'bool',
        'anonymityLevel' => 'string',
        'flatRateEnabled' => 'bool',
        'rateCommissionSafeCheckout' => 'float'
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      * @phpstan-var array<string, string|null>
      * @psalm-var array<string, string|null>
      */
    protected static $openAPIFormats = [
        'name' => null,
        'vatNumber' => null,
        'commercialRegistryNumber' => null,
        'websiteUrl' => null,
        'customBaseUrl' => null,
        'billingAddress' => null,
        'primaryColor' => null,
        'secondaryColor' => null,
        'accentColor' => null,
        'errorColor' => null,
        'infoColor' => null,
        'successColor' => null,
        'warningColor' => null,
        'endUserNotificationToggle' => null,
        'anonymityLevel' => null,
        'flatRateEnabled' => null,
        'rateCommissionSafeCheckout' => null
    ];

    /**
      * Array of nullable properties. Used for (de)serialization
      *
      * @var boolean[]
      */
    protected static array $openAPINullables = [
        'name' => false,
		'vatNumber' => true,
		'commercialRegistryNumber' => false,
		'websiteUrl' => true,
		'customBaseUrl' => true,
		'billingAddress' => true,
		'primaryColor' => true,
		'secondaryColor' => true,
		'accentColor' => true,
		'errorColor' => true,
		'infoColor' => true,
		'successColor' => true,
		'warningColor' => true,
		'endUserNotificationToggle' => false,
		'anonymityLevel' => false,
		'flatRateEnabled' => false,
		'rateCommissionSafeCheckout' => false
    ];

    /**
      * If a nullable field gets set to null, insert it here
      *
      * @var boolean[]
      */
    protected array $openAPINullablesSetToNull = [];

    /**
     * Array of property to type mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function openAPITypes()
    {
        return self::$openAPITypes;
    }

    /**
     * Array of property to format mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function openAPIFormats()
    {
        return self::$openAPIFormats;
    }

    /**
     * Array of nullable properties
     *
     * @return array
     */
    protected static function openAPINullables(): array
    {
        return self::$openAPINullables;
    }

    /**
     * Array of nullable field names deliberately set to null
     *
     * @return boolean[]
     */
    private function getOpenAPINullablesSetToNull(): array
    {
        return $this->openAPINullablesSetToNull;
    }

    /**
     * Setter - Array of nullable field names deliberately set to null
     *
     * @param boolean[] $openAPINullablesSetToNull
     */
    private function setOpenAPINullablesSetToNull(array $openAPINullablesSetToNull): void
    {
        $this->openAPINullablesSetToNull = $openAPINullablesSetToNull;
    }

    /**
     * Checks if a property is nullable
     *
     * @param string $property
     * @return bool
     */
    public static function isNullable(string $property): bool
    {
        return self::openAPINullables()[$property] ?? false;
    }

    /**
     * Checks if a nullable property is set to null.
     *
     * @param string $property
     * @return bool
     */
    public function isNullableSetToNull(string $property): bool
    {
        return in_array($property, $this->getOpenAPINullablesSetToNull(), true);
    }

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @var string[]
     */
    protected static $attributeMap = [
        'name' => 'name',
        'vatNumber' => 'vatNumber',
        'commercialRegistryNumber' => 'commercialRegistryNumber',
        'websiteUrl' => 'websiteUrl',
        'customBaseUrl' => 'customBaseUrl',
        'billingAddress' => 'billingAddress',
        'primaryColor' => 'primaryColor',
        'secondaryColor' => 'secondaryColor',
        'accentColor' => 'accentColor',
        'errorColor' => 'errorColor',
        'infoColor' => 'infoColor',
        'successColor' => 'successColor',
        'warningColor' => 'warningColor',
        'endUserNotificationToggle' => 'endUserNotificationToggle',
        'anonymityLevel' => 'anonymityLevel',
        'flatRateEnabled' => 'flatRateEnabled',
        'rateCommissionSafeCheckout' => 'rateCommissionSafeCheckout'
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'name' => 'setName',
        'vatNumber' => 'setVatNumber',
        'commercialRegistryNumber' => 'setCommercialRegistryNumber',
        'websiteUrl' => 'setWebsiteUrl',
        'customBaseUrl' => 'setCustomBaseUrl',
        'billingAddress' => 'setBillingAddress',
        'primaryColor' => 'setPrimaryColor',
        'secondaryColor' => 'setSecondaryColor',
        'accentColor' => 'setAccentColor',
        'errorColor' => 'setErrorColor',
        'infoColor' => 'setInfoColor',
        'successColor' => 'setSuccessColor',
        'warningColor' => 'setWarningColor',
        'endUserNotificationToggle' => 'setEndUserNotificationToggle',
        'anonymityLevel' => 'setAnonymityLevel',
        'flatRateEnabled' => 'setFlatRateEnabled',
        'rateCommissionSafeCheckout' => 'setRateCommissionSafeCheckout'
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'name' => 'getName',
        'vatNumber' => 'getVatNumber',
        'commercialRegistryNumber' => 'getCommercialRegistryNumber',
        'websiteUrl' => 'getWebsiteUrl',
        'customBaseUrl' => 'getCustomBaseUrl',
        'billingAddress' => 'getBillingAddress',
        'primaryColor' => 'getPrimaryColor',
        'secondaryColor' => 'getSecondaryColor',
        'accentColor' => 'getAccentColor',
        'errorColor' => 'getErrorColor',
        'infoColor' => 'getInfoColor',
        'successColor' => 'getSuccessColor',
        'warningColor' => 'getWarningColor',
        'endUserNotificationToggle' => 'getEndUserNotificationToggle',
        'anonymityLevel' => 'getAnonymityLevel',
        'flatRateEnabled' => 'getFlatRateEnabled',
        'rateCommissionSafeCheckout' => 'getRateCommissionSafeCheckout'
    ];

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @return array
     */
    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @return array
     */
    public static function setters()
    {
        return self::$setters;
    }

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @return array
     */
    public static function getters()
    {
        return self::$getters;
    }

    /**
     * The original name of the model.
     *
     * @return string
     */
    public function getModelName()
    {
        return self::$openAPIModelName;
    }

    public const ANONYMITY_LEVEL_COMPLETE = 'COMPLETE';
    public const ANONYMITY_LEVEL_PARTIAL_FIRST_NAME = 'PARTIAL_FIRST_NAME';
    public const ANONYMITY_LEVEL_TRANSPARENT = 'TRANSPARENT';

    /**
     * Gets allowable values of the enum
     *
     * @return string[]
     */
    public function getAnonymityLevelAllowableValues()
    {
        return [
            self::ANONYMITY_LEVEL_COMPLETE,
            self::ANONYMITY_LEVEL_PARTIAL_FIRST_NAME,
            self::ANONYMITY_LEVEL_TRANSPARENT,
        ];
    }

    /**
     * Associative array for storing property values
     *
     * @var mixed[]
     */
    protected $container = [];

    /**
     * Constructor
     *
     * @param mixed[] $data Associated array of property values
     *                      initializing the model
     */
    public function __construct(array $data = null)
    {
        $this->setIfExists('name', $data ?? [], null);
        $this->setIfExists('vatNumber', $data ?? [], null);
        $this->setIfExists('commercialRegistryNumber', $data ?? [], null);
        $this->setIfExists('websiteUrl', $data ?? [], null);
        $this->setIfExists('customBaseUrl', $data ?? [], null);
        $this->setIfExists('billingAddress', $data ?? [], null);
        $this->setIfExists('primaryColor', $data ?? [], null);
        $this->setIfExists('secondaryColor', $data ?? [], null);
        $this->setIfExists('accentColor', $data ?? [], null);
        $this->setIfExists('errorColor', $data ?? [], null);
        $this->setIfExists('infoColor', $data ?? [], null);
        $this->setIfExists('successColor', $data ?? [], null);
        $this->setIfExists('warningColor', $data ?? [], null);
        $this->setIfExists('endUserNotificationToggle', $data ?? [], null);
        $this->setIfExists('anonymityLevel', $data ?? [], 'PARTIAL_FIRST_NAME');
        $this->setIfExists('flatRateEnabled', $data ?? [], null);
        $this->setIfExists('rateCommissionSafeCheckout', $data ?? [], null);
    }

    /**
    * Sets $this->container[$variableName] to the given data or to the given default Value; if $variableName
    * is nullable and its value is set to null in the $fields array, then mark it as "set to null" in the
    * $this->openAPINullablesSetToNull array
    *
    * @param string $variableName
    * @param array  $fields
    * @param mixed  $defaultValue
    */
    private function setIfExists(string $variableName, array $fields, $defaultValue): void
    {
        if (self::isNullable($variableName) && array_key_exists($variableName, $fields) && is_null($fields[$variableName])) {
            $this->openAPINullablesSetToNull[] = $variableName;
        }

        $this->container[$variableName] = $fields[$variableName] ?? $defaultValue;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        if ($this->container['endUserNotificationToggle'] === null) {
            $invalidProperties[] = "'endUserNotificationToggle' can't be null";
        }
        if ($this->container['anonymityLevel'] === null) {
            $invalidProperties[] = "'anonymityLevel' can't be null";
        }
        $allowedValues = $this->getAnonymityLevelAllowableValues();
        if (!is_null($this->container['anonymityLevel']) && !in_array($this->container['anonymityLevel'], $allowedValues, true)) {
            $invalidProperties[] = sprintf(
                "invalid value '%s' for 'anonymityLevel', must be one of '%s'",
                $this->container['anonymityLevel'],
                implode("', '", $allowedValues)
            );
        }

        if ($this->container['rateCommissionSafeCheckout'] === null) {
            $invalidProperties[] = "'rateCommissionSafeCheckout' can't be null";
        }
        return $invalidProperties;
    }

    /**
     * Validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properties are valid
     */
    public function valid()
    {
        return count($this->listInvalidProperties()) === 0;
    }


    /**
     * Gets name
     *
     * @return string|null
     */
    public function getName()
    {
        return $this->container['name'];
    }

    /**
     * Sets name
     *
     * @param string|null $name name
     *
     * @return self
     */
    public function setName($name)
    {
        if (is_null($name)) {
            throw new \InvalidArgumentException('non-nullable name cannot be null');
        }
        $this->container['name'] = $name;

        return $this;
    }

    /**
     * Gets vatNumber
     *
     * @return string|null
     */
    public function getVatNumber()
    {
        return $this->container['vatNumber'];
    }

    /**
     * Sets vatNumber
     *
     * @param string|null $vatNumber vatNumber
     *
     * @return self
     */
    public function setVatNumber($vatNumber)
    {
        if (is_null($vatNumber)) {
            array_push($this->openAPINullablesSetToNull, 'vatNumber');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('vatNumber', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['vatNumber'] = $vatNumber;

        return $this;
    }

    /**
     * Gets commercialRegistryNumber
     *
     * @return string|null
     */
    public function getCommercialRegistryNumber()
    {
        return $this->container['commercialRegistryNumber'];
    }

    /**
     * Sets commercialRegistryNumber
     *
     * @param string|null $commercialRegistryNumber commercialRegistryNumber
     *
     * @return self
     */
    public function setCommercialRegistryNumber($commercialRegistryNumber)
    {
        if (is_null($commercialRegistryNumber)) {
            throw new \InvalidArgumentException('non-nullable commercialRegistryNumber cannot be null');
        }
        $this->container['commercialRegistryNumber'] = $commercialRegistryNumber;

        return $this;
    }

    /**
     * Gets websiteUrl
     *
     * @return string|null
     */
    public function getWebsiteUrl()
    {
        return $this->container['websiteUrl'];
    }

    /**
     * Sets websiteUrl
     *
     * @param string|null $websiteUrl websiteUrl
     *
     * @return self
     */
    public function setWebsiteUrl($websiteUrl)
    {
        if (is_null($websiteUrl)) {
            array_push($this->openAPINullablesSetToNull, 'websiteUrl');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('websiteUrl', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['websiteUrl'] = $websiteUrl;

        return $this;
    }

    /**
     * Gets customBaseUrl
     *
     * @return string|null
     */
    public function getCustomBaseUrl()
    {
        return $this->container['customBaseUrl'];
    }

    /**
     * Sets customBaseUrl
     *
     * @param string|null $customBaseUrl customBaseUrl
     *
     * @return self
     */
    public function setCustomBaseUrl($customBaseUrl)
    {
        if (is_null($customBaseUrl)) {
            array_push($this->openAPINullablesSetToNull, 'customBaseUrl');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('customBaseUrl', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['customBaseUrl'] = $customBaseUrl;

        return $this;
    }

    /**
     * Gets billingAddress
     *
     * @return \Tripartie\Tpdk\Model\OrganizationUpdateBillingAddress|null
     */
    public function getBillingAddress()
    {
        return $this->container['billingAddress'];
    }

    /**
     * Sets billingAddress
     *
     * @param \Tripartie\Tpdk\Model\OrganizationUpdateBillingAddress|null $billingAddress billingAddress
     *
     * @return self
     */
    public function setBillingAddress($billingAddress)
    {
        if (is_null($billingAddress)) {
            array_push($this->openAPINullablesSetToNull, 'billingAddress');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('billingAddress', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['billingAddress'] = $billingAddress;

        return $this;
    }

    /**
     * Gets primaryColor
     *
     * @return string|null
     */
    public function getPrimaryColor()
    {
        return $this->container['primaryColor'];
    }

    /**
     * Sets primaryColor
     *
     * @param string|null $primaryColor primaryColor
     *
     * @return self
     */
    public function setPrimaryColor($primaryColor)
    {
        if (is_null($primaryColor)) {
            array_push($this->openAPINullablesSetToNull, 'primaryColor');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('primaryColor', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['primaryColor'] = $primaryColor;

        return $this;
    }

    /**
     * Gets secondaryColor
     *
     * @return string|null
     */
    public function getSecondaryColor()
    {
        return $this->container['secondaryColor'];
    }

    /**
     * Sets secondaryColor
     *
     * @param string|null $secondaryColor secondaryColor
     *
     * @return self
     */
    public function setSecondaryColor($secondaryColor)
    {
        if (is_null($secondaryColor)) {
            array_push($this->openAPINullablesSetToNull, 'secondaryColor');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('secondaryColor', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['secondaryColor'] = $secondaryColor;

        return $this;
    }

    /**
     * Gets accentColor
     *
     * @return string|null
     */
    public function getAccentColor()
    {
        return $this->container['accentColor'];
    }

    /**
     * Sets accentColor
     *
     * @param string|null $accentColor accentColor
     *
     * @return self
     */
    public function setAccentColor($accentColor)
    {
        if (is_null($accentColor)) {
            array_push($this->openAPINullablesSetToNull, 'accentColor');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('accentColor', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['accentColor'] = $accentColor;

        return $this;
    }

    /**
     * Gets errorColor
     *
     * @return string|null
     */
    public function getErrorColor()
    {
        return $this->container['errorColor'];
    }

    /**
     * Sets errorColor
     *
     * @param string|null $errorColor errorColor
     *
     * @return self
     */
    public function setErrorColor($errorColor)
    {
        if (is_null($errorColor)) {
            array_push($this->openAPINullablesSetToNull, 'errorColor');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('errorColor', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['errorColor'] = $errorColor;

        return $this;
    }

    /**
     * Gets infoColor
     *
     * @return string|null
     */
    public function getInfoColor()
    {
        return $this->container['infoColor'];
    }

    /**
     * Sets infoColor
     *
     * @param string|null $infoColor infoColor
     *
     * @return self
     */
    public function setInfoColor($infoColor)
    {
        if (is_null($infoColor)) {
            array_push($this->openAPINullablesSetToNull, 'infoColor');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('infoColor', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['infoColor'] = $infoColor;

        return $this;
    }

    /**
     * Gets successColor
     *
     * @return string|null
     */
    public function getSuccessColor()
    {
        return $this->container['successColor'];
    }

    /**
     * Sets successColor
     *
     * @param string|null $successColor successColor
     *
     * @return self
     */
    public function setSuccessColor($successColor)
    {
        if (is_null($successColor)) {
            array_push($this->openAPINullablesSetToNull, 'successColor');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('successColor', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['successColor'] = $successColor;

        return $this;
    }

    /**
     * Gets warningColor
     *
     * @return string|null
     */
    public function getWarningColor()
    {
        return $this->container['warningColor'];
    }

    /**
     * Sets warningColor
     *
     * @param string|null $warningColor warningColor
     *
     * @return self
     */
    public function setWarningColor($warningColor)
    {
        if (is_null($warningColor)) {
            array_push($this->openAPINullablesSetToNull, 'warningColor');
        } else {
            $nullablesSetToNull = $this->getOpenAPINullablesSetToNull();
            $index = array_search('warningColor', $nullablesSetToNull);
            if ($index !== FALSE) {
                unset($nullablesSetToNull[$index]);
                $this->setOpenAPINullablesSetToNull($nullablesSetToNull);
            }
        }
        $this->container['warningColor'] = $warningColor;

        return $this;
    }

    /**
     * Gets endUserNotificationToggle
     *
     * @return bool
     */
    public function getEndUserNotificationToggle()
    {
        return $this->container['endUserNotificationToggle'];
    }

    /**
     * Sets endUserNotificationToggle
     *
     * @param bool $endUserNotificationToggle endUserNotificationToggle
     *
     * @return self
     */
    public function setEndUserNotificationToggle($endUserNotificationToggle)
    {
        if (is_null($endUserNotificationToggle)) {
            throw new \InvalidArgumentException('non-nullable endUserNotificationToggle cannot be null');
        }
        $this->container['endUserNotificationToggle'] = $endUserNotificationToggle;

        return $this;
    }

    /**
     * Gets anonymityLevel
     *
     * @return string
     */
    public function getAnonymityLevel()
    {
        return $this->container['anonymityLevel'];
    }

    /**
     * Sets anonymityLevel
     *
     * @param string $anonymityLevel anonymityLevel
     *
     * @return self
     */
    public function setAnonymityLevel($anonymityLevel)
    {
        if (is_null($anonymityLevel)) {
            throw new \InvalidArgumentException('non-nullable anonymityLevel cannot be null');
        }
        $allowedValues = $this->getAnonymityLevelAllowableValues();
        if (!in_array($anonymityLevel, $allowedValues, true)) {
            throw new \InvalidArgumentException(
                sprintf(
                    "Invalid value '%s' for 'anonymityLevel', must be one of '%s'",
                    $anonymityLevel,
                    implode("', '", $allowedValues)
                )
            );
        }
        $this->container['anonymityLevel'] = $anonymityLevel;

        return $this;
    }

    /**
     * Gets flatRateEnabled
     *
     * @return bool|null
     */
    public function getFlatRateEnabled()
    {
        return $this->container['flatRateEnabled'];
    }

    /**
     * Sets flatRateEnabled
     *
     * @param bool|null $flatRateEnabled flatRateEnabled
     *
     * @return self
     */
    public function setFlatRateEnabled($flatRateEnabled)
    {
        if (is_null($flatRateEnabled)) {
            throw new \InvalidArgumentException('non-nullable flatRateEnabled cannot be null');
        }
        $this->container['flatRateEnabled'] = $flatRateEnabled;

        return $this;
    }

    /**
     * Gets rateCommissionSafeCheckout
     *
     * @return float
     */
    public function getRateCommissionSafeCheckout()
    {
        return $this->container['rateCommissionSafeCheckout'];
    }

    /**
     * Sets rateCommissionSafeCheckout
     *
     * @param float $rateCommissionSafeCheckout rateCommissionSafeCheckout
     *
     * @return self
     */
    public function setRateCommissionSafeCheckout($rateCommissionSafeCheckout)
    {
        if (is_null($rateCommissionSafeCheckout)) {
            throw new \InvalidArgumentException('non-nullable rateCommissionSafeCheckout cannot be null');
        }
        $this->container['rateCommissionSafeCheckout'] = $rateCommissionSafeCheckout;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     *
     * @param integer $offset Offset
     *
     * @return boolean
     */
    public function offsetExists($offset): bool
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     *
     * @param integer $offset Offset
     *
     * @return mixed|null
     */
    #[\ReturnTypeWillChange]
    public function offsetGet($offset)
    {
        return $this->container[$offset] ?? null;
    }

    /**
     * Sets value based on offset.
     *
     * @param int|null $offset Offset
     * @param mixed    $value  Value to be set
     *
     * @return void
     */
    public function offsetSet($offset, $value): void
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     *
     * @param integer $offset Offset
     *
     * @return void
     */
    public function offsetUnset($offset): void
    {
        unset($this->container[$offset]);
    }

    /**
     * Serializes the object to a value that can be serialized natively by json_encode().
     * @link https://www.php.net/manual/en/jsonserializable.jsonserialize.php
     *
     * @return mixed Returns data which can be serialized by json_encode(), which is a value
     * of any type other than a resource.
     */
    #[\ReturnTypeWillChange]
    public function jsonSerialize()
    {
       return ObjectSerializer::sanitizeForSerialization($this);
    }

    /**
     * Gets the string presentation of the object
     *
     * @return string
     */
    public function __toString()
    {
        return json_encode(
            ObjectSerializer::sanitizeForSerialization($this),
            JSON_PRETTY_PRINT
        );
    }

    /**
     * Gets a header-safe presentation of the object
     *
     * @return string
     */
    public function toHeaderValue()
    {
        return json_encode(ObjectSerializer::sanitizeForSerialization($this));
    }
}


